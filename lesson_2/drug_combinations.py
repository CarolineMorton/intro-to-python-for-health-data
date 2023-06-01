drugs = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Propanolol']

def find_combinations(drugs):
    """
    Find all possible combinations of drugs

    Args:
        drugs (list): list of drugs

    Returns:
        list: list of lists of drug combinations
    """
    combinations = []
    for first_drug in drugs:
        for second_drug in drugs:
            if first_drug != second_drug:
                if [second_drug, first_drug] not in combinations:
                    new_combination = [first_drug, second_drug]
                    combinations.append(new_combination)
    return combinations

print(find_combinations(drugs))

import itertools

drugs = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Propanolol']

def find_combinations(drugs, number_of_drugs):
    """
    Find all possible combinations of drugs

    Args:
        drugs (list): list of drugs
        number_of_drugs (int): number of drugs in each combination

    Returns:
        list: list of lists of drug combinations
    """
    combinations = []
    combinations += list(itertools.combinations(drugs, number_of_drugs))
    return combinations

print(find_combinations(drugs, 2))
print(find_combinations(drugs, 3))