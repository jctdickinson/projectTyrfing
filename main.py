from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from projectTyrfing import *


class projectTyrfing(App):
    def build(self):
        return GUI()


class GUI(GridLayout):
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text="Testing the grid"))

        self.add_widget(Label(text="testing multiple labels"))
        pass


if __name__ == '__main__':
    projectTyrfing().run()
