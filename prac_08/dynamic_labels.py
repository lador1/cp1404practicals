from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # NOTE I DO NOT UNDERSTAND SUPER OR KWARGS L
        self.name_to_label = {"Bob": "Male", "Cat": "Identifies as Dog", "Oreo": "Cookie"}

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_to_label:
            temp_label = Label(text=name)
            self.root.ids.enter_widgets.add_widget(temp_label)


DynamicLabels().run()
