

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Luca'

MILE_IN_KILOMETRE = 1.60934


class MilesToKilometresConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Holds the Miles to KM calculation, value entered from TextInput (validate_miles)
        and outputs result to the output_kilometres ID"""

        value = self.validate_miles()
        result = value * MILE_IN_KILOMETRE
        self.root.ids.output_kilometres.text = f'{str(result)} kilometres' # Calculation outputs to the ID which is specified in the label

    def handle_increment(self, change):
        """Value from text input + change which is specified as 1 or -1 in the kv file."""

        value = self.validate_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def validate_miles(self):
        """Whatever is inputted into the TextInput is associated with the input_miles ID. So Value = input from ID,
        If input is not 0 continue"""
        try:
            value = float(self.root.ids.input_miles.text)  # Input into TextInput
            return value
        except ValueError:
            return 0


MilesToKilometresConverter().run()
