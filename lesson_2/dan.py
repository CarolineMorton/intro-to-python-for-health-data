from typing import Optional
from datetime import datetime



class Patient():
    def __init__(self, date_of_birth, snomed_events=[], icd_events=[]):
        self.age = self.calculate_age(date_of_birth)
        self.snomed_events = snomed_events
        self.icd_events = icd_events

    @staticmethod
    def calculate_age(date_of_birth):
        today = datetime.today()
        age = today.year - date_of_birth.year
        return age
    
    def count_snomed_events(self):
        return len(set(self.snomed_events))
    
    def count_icd_events(self):
        return len(set(self.icd_events))
    
    def calculate_fraility_score(self):
        return round((self.count_snomed_events() + self.count_icd_events())/50) + (self.age/100)

test = Patient(date_of_birth=datetime(1955, 1, 1), snomed_events=[1,2,3,4, 1, 2, 3, 4], icd_events=["x","y","z"])
print(test.age)
print(test.calculate_fraility_score())
