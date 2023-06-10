---
marp: true
theme: default
paginate: true
---

# Session 1: Introduction to Python for Healthcare Researchers

---

## Why Python?

1. **Ease of Learning:** Python's simple and readable syntax

2. **Versatility and Efficiency:** Python's rich ecosystem of libraries and tools make it extremely versatile. Packages such as pandas for data manipulation, matplotlib for data visualization, and scikit-learn for machine learning make Python an efficient tool for health data science.

3. **Reproducibility:** Python's support for scripting allows for reproducibility

4. **Interdisciplinary Usage:** Python is not exclusive to programmers.

---

# Running Python
There are two primary ways to run Python code

1. **Interpreter mode** - type python commands directly into the terminal 

2. **Scripting mode** - write code in a file with a .py extension and run it using Python

---

# Interpreter mode

```bash
python
```

```bash
>>>
```

```
>>> print("Hello, world!")
```

You will get:
```bash
 Hello, world!
```

---
# Scripting mode

`hello.py`
```python
print("Hello, world!")
```

We run this: 
```bash
python hello.py
```

And we get:
```bash
Hello, world!
```

--- 
# :pencil2: Exercise 1

1. Create a python file called `lesson1.py` on your computer using your text editor.
2. Add a print statement and then run this file from the command line. 

---

# :pencil2: Exercise 1 Solution

```python
print("Hello, from lesson1.py")
```

You should get printed to the command line:

```bash
Hello, from lesson1.py
```

---
# Variables
Variables are used to store values. They can be used to store different types of data, such as numbers, text, or logical values.

```python
drug_name = "Aspirin"
quantity = 10
concentration = 2.5
is_prescription_only = True
```

---
# Using variables

```python
print(drug_name)
```

And we get:

```bash
Aspirin
```

We can insert them into strings using f-strings:

```python
print(f"{drug_name} is a drug.")
```

And we get:

```bash
Aspirin is a drug.
```
---

# Operations on variables

```python
print(quantity * concentration)
```

And we get:

```bash
25.0
```
---

# Saving the output of an operation to a variable

```python
total_dose = quantity * concentration
print(total_dose)
```

And we get:

```bash
25.0
```

---
# :pencil2: Exercise 2
> Modify your `lesson1.py` file to include the following:
> 1. Create a variable called `drug_name` and assign it the value `"Aspirin"`.
> 2. Create a variable called `quantity` and assign it the value `10`.
> 3. Create a variable called `text` and use your `drug_name` and `quantity` variables to create the following string: `"Aspirin is a drug that comes in a pack of 10."`.

---
# :pencil2: Exercise 2 Solution

```python
drug_name = "Aspirin"
quantity = 10
text = f"{drug_name} is a drug that comes in a pack of {quantity}."
print(text)
```

You should get printed to the command line:

```bash
Aspirin is a drug that comes in a pack of 10.
```

---
# Comparison operators

```python
quantity = 10
print(quantity == 10)
```

And we get:

```bash
True
```
---
# Comparison operators

We can use the following operators to compare variables:
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

---
# Types

Python has several built-in types. We have already come across several. The most commonly used ones are:

1. **Integers:** Whole numbers, e.g., 3, -2, 10.
2. **Floats:** Real numbers, e.g., 3.2, -0.9, 3.14.
3. **Strings:** Text, e.g., "Aspirin", 'Paracetamol'.
4. **Booleans:** Logical values, either True or False.

```python
drug_name = "Aspirin" # string 
quantity = 10 # integer 
concentration = 2.5 # float 
is_prescription_only = True # boolean`
```

---
# Checking a type

We can check the type of a variable using the `type` function:

```bash
>>> type("aspirin")
```

or from a python file:

```python
print(type("aspirin"))
```

And we get:

```bash
<class 'str'>
```

---
# Converting between types

We can convert some types to others using the following functions but we may lose information in the process:

```python
int(3.14) # 3
float(3) # 3.0
str(3) # "3"
bool(0) # False
```

---
# Check type of a variable

```python
concentration = 2.5
type(concentration) # float
```

---
# Functions

Functions are reusable pieces of code. They take in inputs, perform some actions, and return a result.

```python
def add_two_numbers(x, y):
    return x + y
```

We can then use this function:

```python
add_two_numbers(3, 5) # 8
```

---
# Saving the output of a function to a variable

```python
total = add_two_numbers(3, 5)
print(total) # 8
```

---
# Notes about functions

1. They start with the def keyword.
2. They have a name, in this case, `add_two_numbers`. 
3. They have arguments, in this case, x and y. These are the inputs to the function. You can have as many arguments as you like, including none.
4. They have a return statement. 

---
# :pencil2: Exercise 3

1. Create a new python file called `drug_group1.py`.

2. Create a function called `determine_aspirin_group`  that takes in a drug name and returns the drug group.
3. Test your function by calling it with the following drug name: "Aspirin".

---
# :pencil2: Exercise 3 Solution

```python
def determine_aspirin_group(drug_name):
    return "NSAID"
```

We can now test our function:
```python
print(determine_aspirin_group("Aspirin")) # NSAID
```

---
# Control Flow

If/else statements allow us to perform different actions depending on the value of a variable.

```python
if drug_name == "Aspirin":
    return "NSAID"
else:
    return "Unknown"
```

---
# Control Flow - Multiple conditions
We can also use elif statements to check multiple conditions:

```python
if drug_name == "Aspirin":
    return "NSAID"
elif drug_name == "Paracetamol":
    return "Analgesic"
else:
    return "Unknown"
```

---

# Control Flow - Adding complexity

We can build  up more complex conditions using the following operators:
- `and`: Both conditions must be true.
- `or`: At least one condition must be true.
- `not`: The condition must be false.

---

# :pencil2: Exercise 4

1. Create a function called `get_drug_group` that takes in a drug name and returns the drug group.

| Drug Name   | Drug Group |
| ----------- | ---------- |
| aspirin   | NSAID      |
| paracetamol | Analgesic |
| propranolol | Beta Blocker |
| ibuprofen | NSAID |

2. Test your function by calling it with the following drug names: "Aspirin", "Paracetamol", "Caffeine".

---
# :pencil2: Exercise 4 Solution

```python
def get_drug_group(drug_name):
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

---
# :pencil2: Exercise 4 Solution

We can now test our function:

```python
print(get_drug_group("aspirin")) # NSAID
print(get_drug_group("paracetamol")) # Analgesic
print(get_drug_group("caffeine")) # Unknown
```

---
# In-built functions (known as methods)

Python types have in-built functions that can be used to perform common operations on them. These are known as methods. They are called using the dot notation:

```python
drug_name = "Aspirin"
drug_name.lower() # "aspirin"
```

---

# Examples of in-built functions
## Strings

```python
drug_name = "Aspirin is a drug."
drug_name.lower() # "aspirin is a drug." = converts to lowercase
drug_name.upper() # "ASPIRIN IS A DRUG." = converts to uppercase
drug_name.title() # "Aspirin Is A Drug." = converts to title case
drug_name.replace("drug", "medication") # "Aspirin is a medication." = replaces "drug" with "medication"
```

---

#### Integers and floats

```python
concentration = 2.9
round(concentration) # 3 - rounds to the nearest integer
concentration.is_integer() # False - checks if the number is an integer
```

---
# :pencil2: Exercise 5

Rewrite your `get_drug_group` function to convert the drug name to lowercase before checking it. This will allow the function to work if the user enters the drug name in uppercase. Test it with `"ASPIRIN"` and `"Paracetamol"`.

---

# :pencil2: Exercise 5 Solution
    
```python
def get_drug_group(drug_name):
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

---
## Docstrings

Doc strings are used to document what a function does, its arguments, and what it returns.

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
---

# Data Structures

Python has several built-in data structures. The most commonly used ones are:

1. **List:** A collection of items in a specific order, e.g., ['Aspirin', 'Paracetamol', 'Ibuprofen'].
2. **Set:** A collection of unique items with no specific order, e.g., {'Aspirin', 'Paracetamol'}.
3. **Dictionary:** A collection of key-value pairs, e.g., {'Aspirin': 'NSAID', 'Paracetamol': 'Analgesic'}.

---
# Lists

```python
drug_list = ["Aspirin", "Paracetamol", "Ibuprofen"]
drug_list[0] # "Aspirin" - gets the first item in the list
drug_list[-1] # "Ibuprofen" - gets the last item in the list
```

Python uses zero-based indexing.

```python
drug_list.append("Propranolol") # ["Aspirin", "Paracetamol", "Ibuprofen", "Propranolol"] - adds an item to the end of the list
drug_list.insert(1, "Caffeine") # ["Aspirin", "Caffeine", "Paracetamol", "Ibuprofen"] - inserts an item at a specific index
drug_list.remove("Paracetamol") # ["Aspirin", "Ibuprofen"] - removes an item from the list
drug_list.sort() # ["Aspirin", "Ibuprofen"] - sorts the list alphabetically
```

---
# Sets

Sets are similar as lists but they are unmutable and cannot contain duplicates.

```python
drug_set = {"Aspirin", "Paracetamol", "Ibuprofen", "Aspirin"}
print(drug_set) # {"Aspirin", "Paracetamol", "Ibuprofen"} - duplicates are removed
```

---
# Dictionaries

```python
drug_dict = {"Aspirin": "NSAID", "Paracetamol": "Analgesic", "Ibuprofen": "NSAID"}
drug_dict["Aspirin"] # "NSAID" - gets the value for the given key
drug_dict['Caffeine'] = "Other" # {"Aspirin": "NSAID", "Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Other"} - adds a new key-value pair
drug_dict.pop("Aspirin") # {"Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Stimulant"} - removes a key-value pair
drug_dict['Caffeine'] = "Stimulant" # {"Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Stimulant"} - updates a key-value pair
```

---
# :pencil2: Exercise 6

Modify your `get_drug_group` function to use a dictionary instead of if statements.

```python
def get_drug_group(drug_name):
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

---
# :pencil2: Exercise 6 Solution
    
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
    drug_dict = {
        "aspirin": "NSAID",
        "paracetamol": "Analgesic",
        "propranolol": "Beta Blocker",
        "ibuprofen": "NSAID",
    }
    return drug_dict[drug_name]
```

---
# Loops

Looping allows us to perform the same action multiple times. There are two types of loops in Python: for loops and while loops. For now, we'll focus on for loops.

```python
for drug in ["Aspirin", "Paracetamol", "Ibuprofen"]:
    print(drug)
```

And we get:

```bash
Aspirin
Paracetamol
Ibuprofen
```

---
# Summary

We have covered a lot of ground in this session:

- Running Python
- Variables
- Types
- Functions
- Control Flow
- Data Structures
- For Loops

---
# Homework 
## Task 1: A function that takes in a list of 4 drugs and makes all possible pairs

The drugs to include are:
- Aspirin
- Paracetamol
- Ibuprofen
- Propranolol

## Task 2: Rewrite this so that pairs where the drugs are the same are removed. 

