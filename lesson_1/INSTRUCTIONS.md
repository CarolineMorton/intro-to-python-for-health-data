# Session 1: Introduction to Python for Healthcare Researchers

## 1. Introduction to Python - interpreter vs scripting

Python is a powerful high-level programming language that has become very popular for data analysis in science and engineering.

There are two primary ways to run Python code:

1. **Interpreter mode:** This is the interactive mode. You start a Python interpreter in your terminal, then type Python commands. The interpreter executes each command as it is entered.

```bash
python
```

> :memo: Note
> If you are using a mac, particular an old mac, you may need to type `python3` instead of `python`.

You then enter the python interpreter as evidenced by `>>>`. You do not need to type these.

```bash
>>>
```

 We can now add commands like print. 

```
>>> print("Hello, world!")
```

You will get:
```bash
 Hello, world!
```

2. **Scripting mode:** In this mode, you write your code in a file with a .py extension, then run it using Python. This is useful for more complex programs.

`hello.py`
```python
print("Hello, world!")
```

We run this: 
```sh
python hello.py
```

Now it is over to you:

> :pencil2: **Exercise 1**
> Create a python file called `lesson1.py` on your computer using your text editor.
Add a print statement and then run this file from the command line. 

<details>

<summary>Answer</summary>

1. Create a file called `lesson1.py` using your text editor.
2. Add the following code to the file:

```python
print("Hello, from lesson1.py")
```

You should get printed to the command line:

```bash
Hello, from lesson1.py
```

</details>

## 2. Variables
Variables are used to store values. They can be used to store different types of data, such as numbers, text, or logical values.

```python
drug_name = "Aspirin"
quantity = 10
concentration = 2.5
is_prescription_only = True
```

We can then use these variables in our code:

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

F-strings are a convenient way to insert variables into strings. They are created by adding an f before the string and then using curly braces to insert the variable. They were introduced in Python 3.6. If you are using an older version of Python, you can use the format function instead:

```python
print("{} is a drug.".format(drug_name))
```

We can also perform operations on variables:

```python
print(quantity * concentration)
```

And we get:

```bash
25.0
```

We could save that output to a new variable:

```python
total_dose = quantity * concentration
print(total_dose)
```

And we get:

```bash
25.0
```

> :pencil2: **Exercise 2**
> Modify your `lesson1.py` file to include the following:
> 1. Create a variable called `drug_name` and assign it the value `"Aspirin"`.
> 2. Create a variable called `quantity` and assign it the value `10`.
> 3. Create a variable called `text` and use your `drug_name` and `quantity` variables to create the following string: `"Aspirin is a drug that comes in a pack of 10."`.

<details>
<summary>
Answer
</summary>

1. Create a file called `lesson1.py` using your text editor.
2. Add the following code to the file:

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
</details>

We can also compare variables:

```python
quantity = 10
print(quantity == 10)
```

And we get:

```bash
True
```

We can use the following operators to compare variables:
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

## 3. Types

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

We can check the type of a variable using the type function:

```bash
type("aspirin")
```

And we get something like this:

```bash
<class 'str'>
```

> :memo: Note
> If you are running this from a file, you will need to use the print function to see the output.

```python
print(type("aspirin"))
```

We can convert some types to others using the following functions but we may lose information in the process:

```python
int(3.14) # 3
float(3) # 3.0
str(3) # "3"
bool(0) # False
```

We also use the type function to check the type of a variable:

```python
concentration = 2.5
type(concentration) # float
```

## 3. Functions

Functions are reusable pieces of code. They take in inputs, perform some actions, and return a result.

```python
def add_two_numbers(x, y):
    return x + y
```

We can then use this function:

```python
add_two_numbers(3, 5) # 8
```

We can also save the output to a variable:

```python
total = add_two_numbers(3, 5)
print(total) # 8
```

There are a few things to note about functions:
1. They start with the def keyword.
2. They have a name, in this case, add_two_numbers. It is best to call functions something that describes what they do. The name should be lowercase and use underscores instead of spaces (snake_case). The code will run if you use a name that does not describe the function but it will be harder for humans to understand. 
3. They have arguments, in this case, x and y. These are the inputs to the function. You can have as many arguments as you like, including none.
4. They have a return statement. This is what the function returns. You can have multiple return statements but the function will only return the first one. If you don't have a return statement, the function will return None.

> :pencil2: **Exercise 3**
> 1. Create a new python file called `drug_group1.py`.
> 2. Create a function called `determine_aspirin_group`  that takes in a drug name and returns the drug group.
> 3. Test your function by calling it with the following drug name: "Aspirin".

<details>
<summary>
Answer
</summary>

1. Create a file called `drug_group1.py` using your text editor.
2. Add the following code to the file:

```python
def determine_aspirin_group(drug_name):
    return "NSAID"
```

We can now test our function:
```python
print(determine_aspirin_group("Aspirin")) # NSAID
```
</details>

We can see this is useful but it only works for aspirin and is not very flexible. We can make it more flexible by using if statements. 

## 4. Control flow
If/else statements allow us to perform different actions depending on the value of a variable.

```python
if drug_name == "Aspirin":
    return "NSAID"
else:
    return "Unknown"
```

We can also use elif statements to check multiple conditions:

```python
if drug_name == "Aspirin":
    return "NSAID"
elif drug_name == "Paracetamol":
    return "Analgesic"
else:
    return "Unknown"
```

We can build  up more complex conditions using the following operators:
- `and`: Both conditions must be true.
- `or`: At least one condition must be true.
- `not`: The condition must be false.

> :pencil2: **Exercise 4**
> 1. Create a new python file called `drug_groups2.py`. 
> 2. Create a function called `get_drug_group` that takes in a drug name and returns the drug group.

> Use the following table to determine the drug group: 
> | Drug Name | Drug Group |
> | --------- | ---------- |
> | aspirin   | NSAID      |
> | paracetamol | Analgesic |
> | propranolol | Beta Blocker |
> | ibuprofen | NSAID |

> 3. Test your function by calling it with the following drug names: "Aspirin", "Paracetamol", "Caffeine".
<details>
<summary>
Answer
</summary>

1. Create a file called `drug_groups2.py` using your text editor.
2. Add the following code to the file:

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

We can now test our function:

```python
print(get_drug_group("aspirin")) # NSAID
print(get_drug_group("paracetamol")) # Analgesic
print(get_drug_group("caffeine")) # Unknown
```

</details>

## 4. In-built functions (known as methods)
Python types have in-built functions that can be used to perform common operations on them. These are known as methods. They are called using the dot notation:

```python
drug_name = "Aspirin"
drug_name.lower() # "aspirin"
```

There are a lot of methods for each type and you can see them in the python documentation. We'll look at some of the most commonly used ones.

#### Strings

```python
drug_name = "Aspirin is a drug."
drug_name.lower() # "aspirin is a drug." = converts to lowercase
drug_name.upper() # "ASPIRIN IS A DRUG." = converts to uppercase
drug_name.title() # "Aspirin Is A Drug." = converts to title case
drug_name.replace("drug", "medication") # "Aspirin is a medication." = replaces "drug" with "medication"
```

#### Integers and floats

```python
concentration = 2.9
round(concentration) # 3 - rounds to the nearest integer
concentration.is_integer() # False - checks if the number is an integer
```

> :pencil2: **Exercise 4**
> Rewrite your `get_drug_group` function to convert the drug name to lowercase before checking it. This will allow the function to work if the user enters the drug name in uppercase. Test it with `"ASPIRIN"` and `"Paracetamol"`.

<details>
<summary>
Answer
</summary>

Modify your `get_drug_group` function:
    
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

</details>
## 5. Doc strings

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

## 6. Data Structures

Python has several built-in data structures. The most commonly used ones are:

1. **List:** A collection of items in a specific order, e.g., ['Aspirin', 'Paracetamol', 'Ibuprofen'].
2. **Set:** A collection of unique items with no specific order, e.g., {'Aspirin', 'Paracetamol'}.
3. **Dictionary:** A collection of key-value pairs, e.g., {'Aspirin': 'NSAID', 'Paracetamol': 'Analgesic'}.

#### Lists

```python
drug_list = ["Aspirin", "Paracetamol", "Ibuprofen"]
drug_list[0] # "Aspirin" - gets the first item in the list
drug_list[-1] # "Ibuprofen" - gets the last item in the list
```

> :memo: Note
> Python uses zero-based indexing. This means that the first item in a list has an index of 0, the second item has an index of 1, and so on.

We can also use the following methods:

```python
drug_list.append("Propranolol") # ["Aspirin", "Paracetamol", "Ibuprofen", "Propranolol"] - adds an item to the end of the list
drug_list.insert(1, "Caffeine") # ["Aspirin", "Caffeine", "Paracetamol", "Ibuprofen"] - inserts an item at a specific index
drug_list.remove("Paracetamol") # ["Aspirin", "Ibuprofen"] - removes an item from the list
drug_list.sort() # ["Aspirin", "Ibuprofen"] - sorts the list alphabetically
```

#### Sets
Sets are similar as lists but they are unmutable and cannot contain duplicates.

```python
drug_set = {"Aspirin", "Paracetamol", "Ibuprofen", "Aspirin"}
print(drug_set) # {"Aspirin", "Paracetamol", "Ibuprofen"} - duplicates are removed
```

#### Dictionaries

```python
drug_dict = {"Aspirin": "NSAID", "Paracetamol": "Analgesic", "Ibuprofen": "NSAID"}
drug_dict["Aspirin"] # "NSAID" - gets the value for the given key
drug_dict['Caffeine'] = "Other" # {"Aspirin": "NSAID", "Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Other"} - adds a new key-value pair
drug_dict.pop("Aspirin") # {"Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Stimulant"} - removes a key-value pair
drug_dict['Caffeine'] = "Stimulant" # {"Paracetamol": "Analgesic", "Ibuprofen": "NSAID", "Caffeine": "Stimulant"} - updates a key-value pair
```

> :pencil2: **Exercise 5**
> Modify your `get_drug_group` function to use a dictionary instead of if statements.

<details>
<summary>
Answer
</summary>

Modify your `get_drug_group` function:
    
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

</details>

## 7. Loops

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

## Homework 
We have covered a lot of ground in this session. Now it is time to put it into practice.

### Task 1: A function that takes in a list of 4 drugs and makes all possible pairs

The drugs to include are:
- Aspirin
- Paracetamol
- Ibuprofen
- Propranolol

Try not to use any external packages for this task. The output of this function should be:

```python
[
    ['Aspirin', 'Aspirin'], 
    ['Aspirin', 'Paracetamol'], 
    ['Aspirin', 'Ibuprofen'], 
    ['Aspirin', 'Propranolol'], 
    ['Paracetamol', 'Aspirin'],
    ['Paracetamol', 'Paracetamol'], 
    ['Paracetamol', 'Ibuprofen'], 
    ['Paracetamol', 'Propranolol'], 
    ['Ibuprofen', 'Aspirin'], 
    ['Ibuprofen', 'Paracetamol'
    ['Ibuprofen', 'Ibuprofen'], 
    ['Ibuprofen', 'Propranolol'],
    ['Propranolol', 'Aspirin'], 
    ['Propranolol', 'Paracetamol'], 
    ['Propranolol', 'Ibuprofen'], 
    ['Propranolol', 'Propranolol']
]
```

Note in this first task, we are not removing any duplicates. We'll do that in the next task.

#### Tips
- You will need to use a for loop within a for loop.
- You will need to use the append method to add items to a list.
- The output is a list of lists.

### Task 2: Rewrite this so that pairs where the drugs are the same are removed. 

The output of this function should be:

```python
[
    ['Aspirin', 'Paracetamol'], 
    ['Aspirin', 'Ibuprofen'], 
    ['Aspirin', 'Propranolol'], 
    ['Paracetamol', 'Aspirin'],, 
    ['Paracetamol', 'Ibuprofen'], 
    ['Paracetamol', 'Propranolol'], 
    ['Ibuprofen', 'Aspirin'], 
    ['Ibuprofen', 'Paracetamol'
    ['Ibuprofen', 'Propranolol'],
    ['Propranolol', 'Aspirin'], 
    ['Propranolol', 'Paracetamol'], 
    ['Propranolol', 'Ibuprofen'],  
]
```

#### Tips
- You will need to use a for loop within a for loop.
- Think about how you can check if two items are equal. 

This is just the start of your Python journey. There's so much more to learn, but with these basics, you're well on your way. Remember, practice makes perfect!

I will post the answers to the homework on the Tuesday before the next session. If you have any questions, please add them to the [issues](https://github.com/CarolineMorton/intro-to-python-for-health-data/issues) on GitHub. You will have to create a GitHub account if you don't already have one to do this. 