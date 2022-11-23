from prac_09.car import Car
import random


class UnreliableCar(Car):
    """A unreliable car is a car"""

    def __init__(self, reliability: float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Test reliability of car (Set to 50), if random number is higher than 50 than it will drive"""
        number = random.randint(0, 100)
        if number > self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance














