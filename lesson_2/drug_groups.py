import csv

def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
    try:
        drug_name = drug_name.lower()
        for row in reference_data:
            if drug_name in row:
                return row[1]
    except:
        if type(drug_name) == str:
            raise ValueError(f"Drug name: {drug_name} not found in reference data")
        else:
            raise ValueError(f"Drug name: {drug_name} is not a valid drug name")

# print(get_drug_group(1))
print(get_drug_group("penicillin"))