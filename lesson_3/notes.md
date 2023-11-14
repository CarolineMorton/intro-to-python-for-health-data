## Introduction

In this lesson, we will be learning about the following concepts:

- Jupyter Notebooks
- Virtual Environments
- Introduction to Pandas

---

## Homework

### Task 1
Create a new function named `get_user_input` that prompts the user for input and returns the input.

```python
def get_user_input(prompt_message):
    user_input = input(prompt_message)
    return user_input
```

---
### Task 2
Write a new function named `validate_input` that ensures the provided input is a string. This function should:

1. Accept a single argument - the user's input.
2. Validate the input to ensure it is a string, and is not empty.
2. Return the validated input.

---
```python
def validate_input(user_input):
    if type(user_input) == str and user_input != "":
        return user_input
    else:
        return None
```
---
We could add an error message to the `else` statement to tell the user what went wrong. 

```python
def validate_input(user_input):
    if type(user_input) == str and user_input != "":
        return user_input
    else:
        raise ValueError("Input must be a string and cannot be empty.")
```
---
What happens when you pass in a number?

It still passes because user input is always a string. We need to add another condition to check that the input is not empty.

```python
def validate_input(user_input):
    # type will always be a string. Should check is not a number. 
    if user_input != "" and user_input.isalpha():
        return user_input
    else:
        return None
```
---
We could use isnumeric() to check if the input is a number. However, this will not work for decimal numbers. 

```python
def validate_input(user_input):
    # type will always be a string. Should check is not a number. 
    if user_input != "" and user_input.isnumeric() is False:
        return user_input
    else:
        return None
```
---
## Extra credit tasks (Optional):
1. Ensure that the input prompt is repeated until the user provides valid input. 

```python
def get_user_input(prompt_message):
    user_input = input(prompt_message)
    while validate_input(user_input) is None:
        user_input = input(prompt_message)
    return user_input
```

---

This involves using a while loop. The while loop will keep repeating until the condition is met. In this case, the condition is that the input is not None.

We are also using the validate_input function to check if the input is valid within the while loop. This is incontrast to a more functional approach where we would run the functions sequentially. It is a matter of preference but I find this approach more readable.

---

2. Add an extra validation to check that there are no whitespaces in or around the user input. 

```python
def validate_input(user_input):
    # type will always be a string. Should check is not a number. 
    if user_input != "" and user_input.isalpha() and user_input.strip() == user_input:
        return user_input
    else:
        return None
```

---

### Task 3
Integrate User Input and Validation with `get_drug_group`

```python
drug_name = get_user_input("Enter the drug: ")
drug_group = get_drug_group(drug_name)
print(f"The drug group for {drug_name} is {drug_group}.")

```

---

## Jumping into Jupyter Notebooks
Jupyter Notebooks are a great way to write and share code. Think of them as lab notebooks for your code. 

We need to install Jupyter Notebooks. We can do this using pip. 

```bash
pip install jupyterlab
```

or on mac

```bash
pip3 install jupyterlab
```
---

Once installed, we can run Jupyter Notebooks using the following command:

```bash
jupyter lab
```

This will open a new tab in your browser. You can then create a new notebook by clicking on the Python 3 icon.

We can step through the code by pressing the play button. You do have keep track of the order of execution. This indicated by the number in the square brackets.

---

## Introduction to Virtual Environments
Virtual environments are a way to isolate your Python environment. This is useful when you are working on multiple projects that require different versions of Python or different packages.

Let's look at what we have installed in global environment.

```bash
pip list
```

You will see a list of packages that are installed. This might be fine for one project but what if we want to use a different version of a package for another project?

---

We can create a virtual environment using the following commands:

```bash
pip install virtualenv

python -m virtualenv venv
```

This will create a new folder called venv. We can then activate the virtual environment using the following command:

```bash
source venv/bin/activate
```

---

Now we can check what we have installed using the following command:

```bash
pip list
```

We can close the virtual environment using the following command:

```bash
deactivate
```

---

## Introduction to Pandas
Pandas is a Python library that is used for data analysis. It is built on top of NumPy and is one of the most popular libraries for data analysis.

We can install Pandas using the following command:

```bash
pip install pandas
```

---

### DataFrames
DataFrames are the primary data structure in Pandas. They are similar to a spreadsheet or a table in a database.

We can create a DataFrame using the following code:

```python
import pandas as pd

df = pd.read_csv("drug_groups.csv")
```

---

### Classes
Classes are a way to group data and functions together. They are a way to create your own data types. We will be covering classes in more detail in a later lesson.

Let's look at the DataFrame class. We can use the type function to check the type of an object.

```python
type(df)
```

This will return the following:

```bash
pandas.core.frame.DataFrame
```

We can see that the type of df is a DataFrame. This is a class that is part of the Pandas library.

---

### Attributes
Attributes are variables that are part of a class. We can access them using the dot notation.

```python
df.shape
```

### Methods
Methods are functions that are part of a class. We can access them using the dot notation.

```python
df.head()
```

---

### About Classes and Objects
A class is a blueprint for creating objects. An object is an instance of a class.

Everything in Python is an object. This means that everything has attributes and methods.

We have come across a few classes already. For example, str is a class that is used to represent strings. 

```python
name = "Caroline"
type(name)
```

This will return the following:

```bash
str
```

---

We have also come across the methods that are part of the str class. For example, the lower method.

```python
name.lower()
```

In Python, the design philosophy is to favour methods over attibutes so most of the standard library classes will have more methods than attributes, and the attributes might be dunder methods (`__name__`).
In other libraries such as Pandas, there will be lots of use of attributes.

---

### Homework
We are going to be using pandas to merge the information from the drug_groups.csv file with the side_effects.csv file. There are a few steps:

1. Read in the drug_groups.csv file into a DataFrame and store it in a variable called drug_groups.
2. Read in the side_effects.csv file into a DataFrame and store it in a variable called side_effects.
3. Do some data exploration and cleaning of the side_effects DataFrame. You should check for missing values and remove any rows that have missing values.
4. Merge the drug_groups and side_effects DataFrames into a new DataFrame called drug_groups_with_side_effects. You should use the drug_name column to merge the DataFrames.
5. Save the drug_groups_with_side_effects DataFrame to a CSV file called drug_groups_with_side_effects.csv.

---
#### Additional tasks (Optional)
1. Create a new column called side_effect_count that contains the number of side effects for each drug.
This will involve splitting the side_effect column on the comma and then counting the number of items in the list.
2. Expand the side_effects DataFrame so that each side effect is in a separate row. You will need to use the explode method.
3. Combine this with the drug_groups DataFrame so that each drug is in a separate row. 