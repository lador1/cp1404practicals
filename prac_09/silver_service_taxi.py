from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, fanciness: float, **kwargs):
        super().__init__(**kwargs)
        self.fanciness = fanciness
        # update class variable
        self.price_per_km *= fanciness

    def get_fare(self):
        # the get_fare() is run in taxi, which grabs the price_per_km which has been updated above
        return super().get_fare() + self.flag_fall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall}"
