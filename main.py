import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionButton
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FadeTransition
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Builder.load_file('derpalgorithmus.kv')

class PersonsScreen(Screen):
    pass

class ConditionsScreen(Screen):
    pass

class ResultsScreen(Screen):
    pass

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(PersonsScreen(name='persons'))
sm.add_widget(ConditionsScreen(name='conditions'))
sm.add_widget(ResultsScreen(name='results'))

class DerPAlgorithmus(App):

    def build(self):
        return sm


if __name__ == '__main__':
    DerPAlgorithmus().run()
