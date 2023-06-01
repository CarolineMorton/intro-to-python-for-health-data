import csv
import re

class Drug():
    """
    A class to represent a drug.

    Attributes
    ----------
    name : str
        The name of the drug.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the drug object.

        Parameters
        ----------
            name (str): The name of the drug.
        """
        self.name = name

    def get_drug_group(self):
        """
        Determines the group of a drug based on its name.

        Returns
        -------
        str
            The group of the drug.
        """
        reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
        try:
            drug_name = self.name.lower()
            for row in reference_data:
                if drug_name in row:
                    return row[1]
        except:
            if type(drug_name) == str and len(drug_name) > 0:
                raise ValueError(f"Drug name: {drug_name} not found in reference data")
            else:
                raise ValueError(f"Drug name: {drug_name} is not a valid drug name")

    def get_side_effects(self):
        """
        Returns the side effects of the drug.

        Returns
        -------
        list
            The side effects of the drug as a list of strings.
        """
        side_effects_data = csv.reader(open("side_effects.csv"), delimiter=",")
        try:
            drug_name = self.name.lower()
            for row in side_effects_data:
                if drug_name in row:
                    # Split by commas and 'or', remove leading and trailing spaces and make lowercase
                    side_effects = row[1].replace(", or ", ", ")
                    side_effects = side_effects.split(", ")
                    side_effects = [side_effect.strip().lower() for side_effect in side_effects]
                    return side_effects
        except:
            if type(drug_name) == str and len(drug_name) > 0:
                raise ValueError(f"Drug name: {drug_name} not found in side effects data")
            else:
                raise ValueError(f"Drug name: {drug_name} is not a valid drug name")

# aspirin = Drug("Aspirin")
# print(aspirin.name)
# print(aspirin.get_drug_group())
# print(aspirin.get_side_effects())

import itertools

drugs = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Propranolol']

def find_combinations(drugs):
    """
    Find all possible combinations of drugs

    Args:
        drugs (list): list of drugs

    Returns:
        list: list of lists of drug combinations
    """
    # create a list of all possible combinations of drugs
    combinations = []
    combinations += list(itertools.combinations(drugs, 2))
    for i in combinations:
        print(f"Combination: {i}")

   # Loop through the combinations and run the checks
    combinations_to_remove = []

    for combination in combinations:
        drug_1 = Drug(combination[0])
        drug_2 = Drug(combination[1])

        print(f"\nChecking {combination} - {drug_1.name} and {drug_2.name}")

        # check if the combinations have the same drug group
        if drug_1.get_drug_group() == drug_2.get_drug_group():
            combinations_to_remove.append(combination)
            print(f"Marked {combination} for removal because of drug group")
        
        else:
            # check if any of the combinations have the same side effect
            side_effects_1 = set(drug_1.get_side_effects())
            side_effects_2 = set(drug_2.get_side_effects())
            common_side_effects = side_effects_1 & side_effects_2
            if len(common_side_effects) > 0:
                combinations_to_remove.append(combination)
                print(f"Marked {combination} for removal because of side effect {common_side_effects}")

    # Remove the combinations that need to be removed
    for combination in combinations_to_remove:
        combinations.remove(combination)

    return combinations


results = find_combinations(drugs)
print("\nFinal results:")
print(results)
