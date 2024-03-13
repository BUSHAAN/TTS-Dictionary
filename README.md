# TTS-Dictionary

## Description
This is a personal project that implements an English-English dictionary application with Text-To-Speech functionality.

## Features
* Look up the definition of English words.
* Listen to the pronunciation of the word and its definition using Text-To-Speech.
  
## Dependencies:

* **pygame**: A popular Python library for multimedia programming, including building games and graphical user interfaces (GUIs). It provides functionalities for sound, graphics, input, and event handling. Used for creating the application window and managing user interactions in the dictionary app.
* **PyQt6**: Another Python library for creating cross-platform desktop applications with a modern and user-friendly interface. Used to build the GUI elements like the search field, buttons, and definition display in this project.
* **gtts**: The Google Text-to-Speech (gTTS) Python library allows you to convert text to audio speech files. Used to convert the word and its definition into spoken audio for playback.
* **Free Dictionary API**: (https://dictionaryapi.dev/) This external API provides access to a free dictionary database. the application interacts with this API to retrieve word definitions.

## Installation

1. Ensure you have Python 3 installed (https://www.python.org/downloads/).
2. Install the required libraries using pip:

```bash
pip install pygame PyQt6 gtts
```
3. Clone or download the project repository.
```bash
git clone https://github.com/BUSHAAN/TTS-Dictionary.git
```
4. Open a terminal in the project directory and run:
```bash
python TTS_dictionary.py
```
## Preview
![Alt text](images/Screenshot_1.jpg?raw=true "Preview")
![Alt text](images/Screenshot_2.jpg?raw=true "Preview")
