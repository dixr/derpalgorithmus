import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import SlideTransition

class DerPAlgorithmusGUI(FloatLayout):
    sm = ObjectProperty()
    persons_view = ObjectProperty()
    conditions_view = ObjectProperty()
    results_view = ObjectProperty()

    persons_names = []
    persons_paid = []

    def __init__(self, **kwargs):
        super(DerPAlgorithmusGUI, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.key_handler)
        for i in range(4):
            self.button_plus()  # add 4 persons by default

    def key_handler(self, instance, key, *largs):
        if key == 27:  # back button in Android
            self.button_prev()
            return True

    def button_prev(self):
        self.sm.transition = SlideTransition(direction='right')
        if self.sm.current == 'Results':
            self.sm.current = 'Conditions'
        elif self.sm.current == 'Conditions':
            self.sm.current = 'Persons'
        #elif self.sm.current == 'Persons':
        #    App.get_running_app().stop()

    def button_plus(self):
        if self.sm.current == 'Persons':
            self.persons_names.append(
                    TextInput(text='Person '+str(len(self.persons_names)+1),
                              multiline=False, size_hint=(.5,None)))
            self.persons_names[-1].height = self.persons_names[-1].minimum_height
            self.persons_view.add_widget(self.persons_names[-1])

            self.persons_paid.append(
                    TextInput(text='0', multiline=False, size_hint=(.5,None),
                              input_filter='float'))
            self.persons_paid[-1].height = self.persons_paid[-1].minimum_height
            self.persons_view.add_widget(self.persons_paid[-1])


    def button_minus(self):
        if self.sm.current == 'Persons':
            if len(self.persons_names) > 1:
                self.persons_view.remove_widget(self.persons_names.pop())
                self.persons_view.remove_widget(self.persons_paid.pop())

    def button_next(self):
        self.sm.transition = SlideTransition(direction='left')
        if self.sm.current == 'Persons':
            self.sm.current = 'Conditions'
        elif self.sm.current == 'Conditions':
            self.sm.current = 'Results'
            self.show_results()

    def show_results(self):
        has_paid = [float(p.text) for p in self.persons_paid]
        to_pay = sum(has_paid) / len(has_paid)
        results = [round(paid - to_pay,2) for paid in has_paid]

        for c in self.results_view.children[:-1]:
            self.results_view.remove_widget(c)

        for i,r in enumerate(results):
            label_person = Label(text=self.persons_names[i].text, size_hint=(.5,None))
            label_person.size[1] = self.results_view.children[-1].height
            self.results_view.add_widget(label_person)

            if r > 0:
                text = 'gets '+str(r)
            elif r < 0:
                text = 'pays '+str(-r)
            else:
                text = 'does nothing'
            label_result = Label(text=text, size_hint=(.5,None))
            label_result.size[1] = self.results_view.children[-1].height
            self.results_view.add_widget(label_result)

class DerPAlgorithmus(App):

    def build(self):
        return DerPAlgorithmusGUI()


if __name__ == '__main__':
    DerPAlgorithmus().run()
