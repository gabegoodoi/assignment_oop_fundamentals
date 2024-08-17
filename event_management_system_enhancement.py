'''
- Problem Statement:

Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
'''

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        self.participants += 1
    
    def get_participant_count(self):
        print(f"The current participant count is {self.participants}")
        return self.participants

birthday_party = Event('Gabe', 2005, 6)

birthday_party.add_participant()

birthday_party.get_participant_count()

