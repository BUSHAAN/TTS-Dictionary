import sys
import pygame
from PyQt6.QtGui import QIcon
import services
import os
import glob
from gtts import gTTS
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton
)

class DictionaryApp(QWidget):
    playing = False
    word = ''
    definition =''
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("TTS Dictionary")

        main_layout = QVBoxLayout()

        input_label = QLabel("Enter a word:")
        main_layout.addWidget(input_label)

        self.input_text = QLineEdit()
        self.input_text.setFixedHeight(30)
        main_layout.addWidget(self.input_text)


        output_label = QLabel("Definition:")
        main_layout.addWidget(output_label)


        self.output_text = QTextEdit()
        main_layout.addWidget(self.output_text)

        button_layout = QHBoxLayout()


        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_input)
        button_layout.addWidget(self.clear_button)

        self.process_button = QPushButton("Lookup")
        self.process_button.clicked.connect(self.define_word)
        button_layout.addWidget(self.process_button)

        main_layout.addLayout(button_layout)

        self.speak_button = QPushButton("start voice")
        self.speak_button.clicked.connect(self.speak_word)
        button_layout.addWidget(self.speak_button)

        self.setLayout(main_layout)
        pygame.init()
        self.show()

        self.app = QApplication.instance()
        self.app.aboutToQuit.connect(self.cleanup)

    def cleanup(self):
        import glob
        for file in glob.glob("definition_*.mp3"):
            os.remove(file)

    def clear_input(self):
        self.input_text.clear()
        self.output_text.clear()
        self.definition=''
        try:
            for file in glob.glob("definition_*.mp3"):
                os.remove(file)
        except FileNotFoundError:
            pass
        except AttributeError:
            pass

    def define_word(self):
        self.word = self.input_text.text()
        if self.word:
            self.definition = services.get_definition(self.word)
            self.output_text.setText(self.definition)
        else:
            self.output_text.setText("Enter a word")

    def speak_word(self):
        word = self.input_text.text()
        if self.definition == "Word not found.":
            self.play_defaults("default_audio\word_not_found.mp3")
        elif not self.input_text.text():
            self.play_defaults("default_audio\enter_a_word.mp3")
        elif self.input_text.text() and not self.definition:
            self.play_defaults("default_audio\lookup_first.mp3")
        else:
            self.to_speech(word,self.definition)
    
    
    def to_speech(self,word,definition):
        if not self.playing:
            self.playing = True
            self.speak_button.setText('Stop voice')
            tts = gTTS(definition)
            tts.save(f'definition_{word}.mp3')
            pygame.mixer.music.load(f'definition_{word}.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.event.get()
                self.clear_button.setEnabled(False)
            self.clear_button.setEnabled(True)
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.playing = False
            self.speak_button.setText('Start voice')
        pygame.mixer.music.unload()

    def play_defaults(self,audio):
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.event.get()
        pygame.mixer.music.unload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryApp()
    sys.exit(app.exec())
