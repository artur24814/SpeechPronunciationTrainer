from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
#download kivy
Builder.load_file('trainer.kv')
# Builder.load_file('drawingspace.kv')
# Builder.load_file('generaloptions.kv')
# Builder.load_file('statusbar.kv')
# Builder.load_file('manwidgets.kv')

class StartWindow(TabbedPanel):
    pass

class MainApp(App):
    def build(self):
        return StartWindow()

if __name__=='__main__':
    MainApp().run()





