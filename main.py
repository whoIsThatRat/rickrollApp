from kivy.app import App
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
sound = SoundLoader.load('rick.wav')

class MainApp(App):
    def build(self):
        img = Image(source = "rick.jpg")
        if sound:
            sound.play()
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()