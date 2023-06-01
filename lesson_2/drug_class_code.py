import csv


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
            

drug = Drug("Aspirin")
print(drug.name)
print(drug.get_drug_group())


class NSAIDs(Drug):
    """
    A class to represent a NSAID.

    Attributes
    ----------
    name : str
        The name of the drug.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the NSAID object.

        Parameters
        ----------
            name (str): The name of the drug.
        """
        super().__init__(name)

    def get_side_effects(self):
        """
        Determines the side effects of a NSAID based on its name.

        Returns
        -------
        str
            The side effects of the NSAID.
        """
        return "Stomach pain, heartburn, nausea, vomiting, diarrhoea, constipation, drowsiness, headache, dizziness, ringing in the ears, trouble concentrating, blurred vision, rash, itching, swelling, or breathing problems"
    

aspirin = NSAIDs("Aspirin")
print(aspirin.name)
print(aspirin.get_drug_group())
print(aspirin.get_side_effects())