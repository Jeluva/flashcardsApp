#main

from kivy.app import App
from kivy.uix.label import Label

class FlashcardsApp(App):
    def build(self):
        return Label(text="¡Hola, Flashcards!")

if __name__ == "__main__":
    FlashcardsApp().run()
