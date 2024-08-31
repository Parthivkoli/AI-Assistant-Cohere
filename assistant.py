import cohere
import speech_recognition as sr
import pyttsx3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import sys

# Initialize Cohere API client with your API key
# Replace 'YOUR_API_KEY' with your actual Cohere API key
co = cohere.Client('YOUR_API_KEY')

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice to a female voice (you can change to other voices as needed)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Assuming the second voice in the list is female

class AssistantThread(QThread):
    gif_animation_signal = pyqtSignal(bool)
    output_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        with sr.Microphone() as source:
            self.gif_animation_signal.emit(True)
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            self.gif_animation_signal.emit(False)
            try:
                command = recognizer.recognize_google(audio)
                self.output_signal.emit(f"User said: {command}")
                self.respond(command)
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                self.speak("Sorry, my speech service is down.")

    def speak(self, text):
        self.gif_animation_signal.emit(True)
        engine.say(text)
        engine.runAndWait()
        self.gif_animation_signal.emit(False)

    def respond(self, command):
        if "your name" in command.lower():
            self.speak("I am your personal AI assistant, powered by Cohere.")
        elif "bye" in command.lower():
            self.speak("Goodbye!")
            QApplication.quit()
        else:
            response = get_cohere_response(command)
            self.output_signal.emit(f"Cohere Response: {response}")
            self.speak(response)

def get_cohere_response(prompt):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100
    )
    return response.generations[0].text.strip()

class AssistantGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Assistant')
        self.setGeometry(100, 100, 500, 600)

        # Create layout
        layout = QVBoxLayout()

        # GIF Label
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignCenter)
        
        # Replace 'path_to_your_gif' with the actual path to your GIF file
        self.movie = QMovie("path_to_your_gif")
        self.gif_label.setMovie(self.movie)
        layout.addWidget(self.gif_label)

        # Status label
        self.status_label = QLabel("Waiting for command...", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Tap to Speak Button
        self.speak_button = QPushButton('Tap to Speak', self)
        self.speak_button.clicked.connect(self.start_listening)
        layout.addWidget(self.speak_button)

        # Text Entry for typing questions
        self.text_entry = QLineEdit(self)
        self.text_entry.setPlaceholderText("Type here")
        layout.addWidget(self.text_entry)

        # Submit Button for text input
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.handle_text_input)
        layout.addWidget(self.submit_button)

        # Output label for displaying responses
        self.output_label = QTextEdit(self)
        self.output_label.setReadOnly(True)
        layout.addWidget(self.output_label)

        # Set layout
        self.setLayout(layout)

        # Initialize Assistant Thread
        self.assistant_thread = AssistantThread()
        self.assistant_thread.gif_animation_signal.connect(self.control_gif_animation)
        self.assistant_thread.output_signal.connect(self.display_output)

        # Initial Greeting
        self.assistant_thread.speak("Hello! I am your AI assistant. How can I help you today?")

    def control_gif_animation(self, is_talking):
        if is_talking:
            self.movie.start()
        else:
            self.movie.stop()
            self.movie.jumpToFrame(0)  # Reset to the first frame

    def display_output(self, text):
        self.output_label.append(text)

    def start_listening(self):
        if not self.assistant_thread.isRunning():
            self.assistant_thread.start()

    def handle_text_input(self):
        question = self.text_entry.text()
        if question:
            response = get_cohere_response(question)
            self.display_output(f"You: {question}")
            self.display_output(f"Assistant: {response}")
            self.assistant_thread.speak(response)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    assistant_gui = AssistantGUI()
    assistant_gui.show()
    sys.exit(app.exec_())
