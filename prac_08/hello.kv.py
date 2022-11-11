from kivy.app import App
from kivy.app import Widget


class HelloWorld(App):
    def build(self):
        self.root = Widget()
        return self.root


HelloWorld().run()
