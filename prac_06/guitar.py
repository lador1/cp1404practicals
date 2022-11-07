CURRENT_YEAR = 2022


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        guitar_age = CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year <= other.year
