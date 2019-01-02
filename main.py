import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FadeTransition, SlideTransition
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class DerPAlgorithmusGUI(BoxLayout):
    sm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DerPAlgorithmusGUI, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.key_handler)

    def key_handler(self, instance, key, *largs):
        if key == 27: # back button in Android is treated as Esc
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        self.sm.transition = SlideTransition(direction='right')
        if self.sm.current == 'Results':
            self.sm.current = 'Conditions'
        elif self.sm.current == 'Conditions':
            self.sm.current = 'Persons'

    def set_next_screen(self):
        self.sm.transition = SlideTransition(direction='left')
        if self.sm.current == 'Persons':
            self.sm.current = 'Conditions'
        elif self.sm.current == 'Conditions':
            self.sm.current = 'Results'

class DerPAlgorithmus(App):

    def build(self):
        return DerPAlgorithmusGUI()


if __name__ == '__main__':
    DerPAlgorithmus().run()
