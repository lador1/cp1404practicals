from musician1 import Musician


class Band(Musician):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} is playing: {self.instruments} ({self.year}) : ${self.__class__}"

    def __str__(self):
        return f"{self.name} is playing: {self.instruments} ({self.year}) : ${self.__class__}"

    def play(self):
        return super().play()
