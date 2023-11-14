# # task 1

# def get_user_input(prompt_message):
#     user_input = input(prompt_message)
#     return user_input

# results = get_user_input("Enter the drug: ")
# print(results)

# # task 2

# def validate_input(user_input):
#     if type(user_input) == str and user_input != "":
#         return user_input
#     else:
#         return None

# user_input = get_user_input("Enter the drug: ")
# validated_results = validate_input(user_input)
# print(validated_results)

# def validate_input(user_input):
#     if type(user_input) == str and user_input != "":
#         return user_input
#     else:
#         raise ValueError("Input must be a string and cannot be empty.")


# def validate_input(user_input):
#     # type will always be a string. Should check is not a number. 
#     if user_input != "" and user_input.isnumeric() is False:
#         return user_input
#     else:
#         return None

# def validate_input(user_input):
#     # type will always be a string. Should check is not a number. 
#     if user_input != "" and user_input.isalpha():
#         return user_input
#     else:
#         return None

## extra credit
# 1

# def get_user_input(prompt_message):
#     user_input = input(prompt_message)
#     while validate_input(user_input) is None:
#         user_input = input(prompt_message)
#     return user_input

# results = get_user_input("Enter the drug: ")
# print(results)

# # 2
def validate_input(user_input):
    # type will always be a string. Should check is not a number. 
    if user_input != "" and user_input.isalpha() and user_input.strip() == user_input:
        return user_input
    else:
        return None

def get_user_input(prompt_message):
    user_input = input(prompt_message)
    while validate_input(user_input) is None:
        user_input = input(prompt_message)
    return user_input

# results = get_user_input("Enter the drug: ")
# print(results)

# task 3
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
    drug_name = drug_name.lower()
    for row in reference_data:
        if drug_name in row:
            return row[1]
    return "Unknown"


drug_name = get_user_input("Enter the drug: ")
drug_group = get_drug_group(drug_name)
print(f"The drug group for {drug_name} is {drug_group}.")