# Session 2: Introduction to Python for Healthcare Researchers
Last session, we covered:
- Intepreter vs Scripts
- Variables
- Types
- Functions
- If/Else Statements
- Docstrings
- Data Structures
- Loops

This session, we will cover:
- Packages
- Reading and Writing Files
- Classes

## Packages and Modules
Modules are collections of functions and classes that are included in the base Python installation. They are created by other developers and can be imported into your code using the `import` command.

For example, in our homework assignment, we had to use find all unique combinations of drug pairs and we did this with a for loop and a list. Your function should have looked something like:

```python
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
            new_combination = [first_drug, second_drug]
            combinations.append(new_combination)
    return combinations

combinations = find_combinations(drugs)
print(combinations)
```

This works but as specified you have some combinations where the drug names are the same, for example, ['Aspirin', 'Aspirin']. We can remove these by adding an if statement to our function:

```python
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
                new_combination = [first_drug, second_drug]
                combinations.append(new_combination)
    return combinations
``` 

This works but we still have some duplicate combinations, for example, ['Ibuprofen', 'Aspirin'] and ['Aspirin', 'Ibuprofen']. We can remove these by adding another if statement to our function:

```python
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
```

Now we have a list of all unique combinations of drugs. This works but it is a lot of code and it is not very readable. Luckily, there is a module called `itertools` that has a function called `combinations` that does exactly what we want. We can import this module and use the function in our code:

```python
import itertools

drugs = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Propanolol']

def find_combinations(drugs):
    """
    Find all possible combinations of drugs

    Args:
        drugs (list): list of drugs

    Returns:
        list: list of lists of drug combinations
    """
    combinations = list(itertools.combinations(drugs, 2))
    return combinations
```

This is much shorter and easier to read. We can also use the `combinations` function to find all combinations of X number drugs:

```python
import itertools

drugs = ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Propanolol']

def find_combinations(drugs):
    """
    Find all possible combinations of drugs

    Args:
        drugs (list): list of drugs
        number_of_drugs (int): number of drugs in each combination

    Returns:
        list: list of lists of drug combinations
    """
    combinations = []
    combinations += list(itertools.combinations(drugs))
    return combinations

print(find_combinations(drugs))
```

Here we have created the same output as our original function but with much less code. What's more is we can extend it to find all combinations of X number of drugs. Try this yourself:

> :pencil2: **Exercise**: Modify the function above to find all combinations of 3 drugs. The function should take in a list of drugs and a number of drugs in each combination and return a list of lists of drug combinations.

<details>
<summary>Answer</summary>

```python

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

```

</details>

The main takeaway here is that there are a lot of modules out there that can make your life easier. You can find a list of all the modules that are included in the base Python installation [here](https://docs.python.org/3/py-modindex.html). 

Packages are collections of functions and classes that are not included in the base Python installation. They are created by other developers and can be installed using the `pip` command. We will be using these packages throughout the course.

## Working with files

There are various ways to read and write files in Python. We will just be concentration on reading in reference data to use in our function. We will be using the `csv` package to read in our data. This package is included in the base Python installation so we don't need to install it. We can import it using the `import` command:

```python
import csv
```

In the first session, we determined drug group based on hard-coded values. As a reminder our function looked like this:

```python
def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    drug_name = drug_name.lower()
    if drug_name == "aspirin":
        return "NSAID"
    elif drug_name == "paracetamol":
        return "Analgesic"
    elif drug_name == "propranolol":
        return "Beta Blocker"
    elif drug_name == "ibuprofen":
        return "NSAID"
    else:
        return "Unknown"
```

This works but it is not very flexible. What if we want to add more drugs? We would have to add more `elif` statements to our function. What if we want to change the group of a drug? We would have to change the function. What if we want to add a new drug group? We would have to change the function. This is not very flexible and it is not very readable. We can improve this by reading in the drug groups from a file. We can create a file called `drug_groups.csv` that looks like this:

| drug_name | drug_group |
| --------- | ---------- |
| aspirin   | NSAID      |
| ibuprofen | NSAID      |
| paracetamol | Analgesic |
| propranolol | Beta Blocker |

We can then read in this file using the `csv` package:

```python
import csv

def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    drug_name = drug_name.lower()
    reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
    for row in reference_data:
        if drug_name in row:
            return row[1]
    
print(get_drug_group("aspirin"))
```

Here we have used the `csv.reader` function to read in the data from the file. We have then looped through each row in the file and checked if the drug name is in the row. If it is, we return the drug group. This is much more flexible and readable. We can add more drugs to the file without changing the function. We can change the group of a drug by changing the file. We can add a new drug group by adding a new row to the file. Try this yourself:

> :pencil2: **Exercise 2**:
> 1. Open up the `drug_groups.csv` file and add a new drug called "Atenolol" with the drug group "Beta Blocker".
> 2. Modify the `get_drug_group` function to return "Unknown" if the drug is not in the file.

<details>
<summary>Answer</summary>

```python
import csv

def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    drug_name = drug_name.lower()
    reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
    for row in reference_data:
        if drug_name in row:
            return row[1]
    return "Unknown"

```
</details>

## Error Handling
In data science, we often have to deal with messy data. This means that we have to deal with errors. For example, we might have a list of drug names that contains a drug that is not in our reference data. We can handle this by adding an `if` statement to our function as seen before. 

There is a choice to be made here. We can either decide to fail early and loudly - i.e. the program stops running if provided with a drug name that is not in the reference dataset so we can investigate why this is the case - or we can decide to continue - i.e. the program continues running but returns "Unknown".  The choice is yours.

This is important when dealing with messy data because sometimes the data contains information that we have not predicted we might need to account for. 
For example, we might get a list of drug names to run though our `get_drug_group` function that contains an item that is a drug name that is not in our reference data. We could predict this is the case and add an `if` statement to handle this. What happens if we get a list of drug names that contains an item that is not a string or is just a blank string? It will fail immediately once you try to call the `lower()` function on it.

Let's try this:

```python
import csv

def get_drug_group(drug_name):
    """
    Determines the group of a drug based on its name.

    Args:
        drug_name (str): The name of the drug.

    Returns:
        str: The group of the drug.
    """
    drug_name = drug_name.lower()
    reference_data = csv.reader(open("drug_groups.csv"), delimiter=",")
    for row in reference_data:
        if drug_name in row:
            return row[1]
    return "Unknown"

group = get_drug_group(1)
print(group)
```

This will fail with the following error:

```bash
Traceback (most recent call last):
  File "error_handling.py", line 18, in <module>
    group = get_drug_group(1)
  File "error_handling.py", line 10, in get_drug_group
    drug_name = drug_name.lower()
AttributeError: 'int' object has no attribute 'lower'
```

We can improve this by using `try` and `except` statements. For example, we can modify our `get_drug_group` function to use a `try` and `except` statement:

```python
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
        raise ValueError(f"Drug name: {drug_name} not found in reference data")

```

Now if we run the function with an integer, it will fail but it will fail with a more useful error message:

```bash
ValueError: Drug name: 1 not found in reference data
```

We could add multiple `except` statements to handle different types of errors. For example, we could add an `except` statement to handle the case where the drug name is not in the reference data:

```python
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
        if type(drug_name) == str and len(drug_name) > 0:
            raise ValueError(f"Drug name: {drug_name} not found in reference data")
        else:
            raise ValueError(f"Drug name: {drug_name} is not a valid drug name")

```

Now if we run this function with various options, we get the following error messages:

```python
print(get_drug_group(1))
```

```bash
ValueError: Drug name: 1 is not a valid drug name
```

```python
print(get_drug_group("penicillin"))
```

```bash
ValueError: Drug name: penicillin not found in reference data
```

When you are first creating your code, it is a good idea to raise lots of errors to see what sort of problems there are with your data and then add in ways to handle these errors. This will help you to create more robust code.

## Classes
Classes are a way of grouping together functions and variables. They are useful when you have a lot of functions and variables that are related to each other. For example, we could create a class called `Drug` that contains a function to get the drug group and a variable to store the drug name:

```python
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
```

Here we have created a class called `Drug` that contains a function called `get_drug_group` and a variable called `name`. We can create an instance of this class by calling the class name and passing in the drug name:

```python
drug = Drug("Aspirin")
print(drug.name)
print(drug.get_drug_group())
``` 

This will print out the drug name and the drug group. We can create multiple instances of this class:

```python
drug_1 = Drug("Aspirin")
drug_2 = Drug("Ibuprofen")
print(drug_1.name)
print(drug_1.get_drug_group())
print(drug_2.name)
print(drug_2.get_drug_group())
```

We get the following output:

```bash
Aspirin
NSAID
Ibuprofen
NSAID
```

Classes allow us to group both data and functions together. In fact everything in Python is a class. When we used `.lower()` on a string, we were in fact using the `lower()` function of the `str` class. Functions that belong to classes are called methods. For example, the `lower()` function is a method of the `str` class. The `append()` function is a method of the `list` class. The `keys()` function is a method of the `dict` class. We can create our own methods by creating our own classes.

### The Power of Classes
Classes allow us to impose structure on the data that we are working on. They can inherit from each other and interact with each other. 

For example, we could create a class called NSAIDs that inherits from the Drug class:

```python
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
```

We can then make a new instance of this class:

```python
aspirin = NSAIDs("Aspirin")
print(aspirin.name)
print(aspirin.get_drug_group())
print(aspirin.get_side_effects())
```

This will print out the drug name, the drug group and the side effects:

```bash
Aspirin
NSAID
Stomach pain, heartburn, nausea, vomiting, diarrhoea, constipation, drowsiness, headache, dizziness, ringing in the ears, trouble concentrating, blurred vision, rash, itching, swelling, or breathing problems
```

Here we have not defined `.get_drug_group()` but it has been inherited from the parent class. 

## Homework
We have covered a lot of material here and it will be worth going through this again and attempting the following home questions:

1. Extend the Drug class to include a function that returns the side effects of the drug. You can find a reference list of side effects in the `side_effects.csv` file.

| drug_name | side_effect |
| --------- | ----------- |
| aspirin   | Stomach pain, heartburn, nausea, or vomiting |
| ibuprofen | Stomach pain, heartburn, nausea, swelling, or breathing problems |
| paracetamol | Nausea|
| propranolol | Dizziness, lightheadedness, or breathing problems |

Tips:
- You will need to read in the side effects file using the `csv` package.
- You will need to add a new variable to the Drug class to store the side effects.
- You will need to consider how to handle a list of side effects and account for both capitalised and non-capitalised side effects, and `or` in the sentence. 

2. Update your `find_combinations` function to take in a list of drugs and find all combinations of 2 drugs where the following conditions are met:
- The drugs are not the same
- The drugs are not in the same drug group
- The drugs do not have the same side effects

Tips:
- You will need to create a new variable for each drug that stores the drug group and side effects.
- You will need to create that new variable from within the function `find_combinations`.
- You will need to find a way to compare the side effects of each drug. Each drug has a list of side effects so you will need to find a way to compare two lists of side effects. Remember we are not looking for an exact match, we are looking for a partial match. For example, if one drug has the side effects "Stomach pain, heartburn, nausea" and another drug has the side effects "Nausea, swelling, or breathing problems", we would consider this a match because the second drug has at least one of the side effects of the first drug.
- Do not alter the list of combinations whilst you are looping through it as this will cause combinations to get skipped. You will need to create a new list of combinations that you want to remove and then remove them after you have finished looping through the list of combinations.

The result should be:
```bash
[
    ['Aspirin', 'Propranolol'], 
    ['Paracetamol', 'Propranolol']
]
```

