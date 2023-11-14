import csv

def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    try:
        print("we are in the try section")
        reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
        drug_name = drug_name.lower()
        for row in reference_data:
            if drug_name in row:
                return row[1]
        
        return "Unknown"
    except:
        print("there is an error here")
        pass

print(get_drug_group("penicillin"))
print(get_drug_group(1))