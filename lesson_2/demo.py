import csv


    

class Drug():
    def __init__(self, name, side_effects):
        self.name = name.capitalize()
        self.side_effects = side_effects

    def get_drug_group(self):
        """
        Determines the group of a drug based on its name.

        Args:
            drug_name (str): The name of the drug.

        Returns:
            str: The group of the drug.
        """
        drug_name = self.name.lower()
        reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
        for row in reference_data:
            if drug_name in row:
                return row[1]
            
    def show_side_effects(self):
        return f"{self.name} has the side effects of {self.side_effects}"
    

class NSAID(Drug):
    def __init__(self, name, side_effects):
        super().__init__(name, side_effects)

    def contraindications(self):
        print(f"{self.name} should not be taken with other NSAIDs.")

class BetaBlocker(Drug):
    def __init__(self, name, side_effects):
        super().__init__(name, side_effects)

    def cautions(self):
        print("Care should be taken in the elderly")

aspirin = NSAID(name="aspirin", side_effects="GI Bleed")
print(aspirin.name)
print(aspirin.get_drug_group())
print(aspirin.show_side_effects())
aspirin.contraindications()

# aspirin = Drug(name="aspirin", side_effects="GI Bleed")
# print(aspirin.name)
# print(aspirin.get_drug_group())
# print(aspirin.show_side_effects())
