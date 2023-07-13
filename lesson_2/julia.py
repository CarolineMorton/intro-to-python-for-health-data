

class PregnantPatient():
    def __init__(self, nhs_number):
        self.nhs_number = nhs_number
    
    def calculate_pregnancy_period():
        pass

    def outcome_of_pregnancy():
        pass


class DataLoader():
    def __init__(self, patients=[]):
        self.patients = patients
        self.nhs_numbers = []

    def load_patients(self, patient):
        if patient.nhs_number not in self.nhs_numbers:
            self.nhs_numbers.append(patient.nhs_number)
            self.patients.append(patient)
        else:
            pass
        print(self.nhs_numbers)

loader = DataLoader()
patient_1 = PregnantPatient(nhs_number=1234567890)
patient_2 = PregnantPatient(nhs_number=9876543210)
patient_3 = PregnantPatient(nhs_number=1234567890)

loader.load_patients(patient_1)
loader.load_patients(patient_2)
loader.load_patients(patient_3)
