from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from projectTyrfing import *


class projectTyrfing(App):
    def build(self):
        return Label(text = "Hello World")

if __name__ == '__main__':
    projectTyrfing().run()