"""
Session 1; start time: 2pm
            end time :
"""
import datetime

from tomlkit import items

COMPLETION_PERCENTAGE = '100'


class Project:
    def __init__(self, name='', start_date="", priority=0.0, cost=0.0, completion_percentage=0.0):
        self.name = name
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """determine if project is complete"""
        return self.completion_percentage == '100'

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"

    def __getitem__(self, item): #used for updating projects
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"
