# AI Assistant Using Cohere

This project is an AI Assistant built using Python, integrating the Cohere API for natural language processing, PyQt5 for the graphical user interface, and SpeechRecognition and pyttsx3 for voice interaction. The assistant can listen to voice commands, process them using Cohere, and respond back in a conversational manner.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Assistant](#running-the-assistant)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Voice Recognition:** Uses Google's SpeechRecognition to convert speech to text.
- **Natural Language Processing:** Processes commands using Cohere's `command-xlarge-nightly` model.
- **Voice Response:** Speaks back the response using pyttsx3.
- **GUI Interface:** A user-friendly GUI built with PyQt5.
- **Text Input:** Option to type queries instead of speaking.

## Prerequisites

- Python 3.6+
- A Cohere API key
- Google SpeechRecognition package
- PyQt5 for GUI
- pyttsx3 for text-to-speech

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Parthivkoli/AI-Assistant-Cohere.git
    cd AI-Assistant-Cohere
    ```

2. **Install the Required Packages:**

    You can install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** The `requirements.txt` should include all necessary libraries:

    ```text
    cohere
    SpeechRecognition
    pyttsx3
    PyQt5
    ```
    

3. **Obtain a Cohere API Key:**

    - Go to [Cohere's website](https://cohere.ai/) and sign up for an API key.
    - Replace the placeholder in the script with your actual API key.

4. **Download the Required GIF:**

    Ensure the GIF file (`Siri_talking2.gif`) is correctly placed in the specified directory within your project. Update the path in the script if needed.

## Running the Assistant

1. **Launch the Assistant:**

    Run the following command to start the application:

    ```bash
    python assistant.py
    ```

2. **Interact with the Assistant:**

    - Use the "Tap to Speak" button to issue voice commands.
    - Alternatively, type questions into the text box and click "Submit."

## Usage

- **Voice Commands:**
    - The assistant listens and responds to various commands.
    - For example, say "What's your name?" to get a response about the assistant's identity.

- **Text Input:**
    - Type a question in the text box and press "Submit."
    - The assistant will process the input and display the response in the GUI.

## Configuration

- **Cohere API Key:** Update the following line with your API key:

    ```python
    co = cohere.Client('your_api_key_here')
    ```

- **Voice Settings:**
    - Modify the voice settings in the script if you want to change the assistant's voice:

    ```python
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Adjust the index for different voices
    ```

- **GIF Path:** Ensure the path to the GIF in the script is correct. Update as needed:

    ```python
    self.movie = QMovie("path/to/your/gif.gif")
    ```
## User Interface
![image](https://github.com/user-attachments/assets/996ba3cf-d1f7-447f-9049-18067be01e91)

## Contributing

Contributions are welcome! If you find bugs, have feature requests, or want to improve the code, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

