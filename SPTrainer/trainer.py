from kivy.uix.boxlayout import BoxLayout

from speach_manager import SpeachManager

class Trainer(BoxLayout):

    def __init__(self, **kwargs):
        super(Trainer, self).__init__(**kwargs)
        self.SpeachManager = SpeachManager()

