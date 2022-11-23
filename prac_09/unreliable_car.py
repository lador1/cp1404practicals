from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, reliability: float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        number = random.randint(0, 100)
        if number > self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance














