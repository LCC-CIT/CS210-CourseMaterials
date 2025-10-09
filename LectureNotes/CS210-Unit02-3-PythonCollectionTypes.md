<h1>Python Collection Types</h1>

**CS 210 Intro to AI Programming**

<h2>Contents</h2>

[toc]

## Lists (Mutable, Ordered, Indexed)

A **list** is an ordered, mutable (changeable) sequence of items. It's the most basic and common collection type in Python. Since they are ordered, you can access items by their index. Lists can contain duplicate elements and a mix of different data types.

| Feature        | Description                                  |
| -------------- | -------------------------------------------- |
| **Syntax**     | Enclosed in square brackets `[]`             |
| **Order**      | **Maintained** (items have a definite order) |
| **Mutability** | **Mutable** (can be changed after creation)  |
| **Duplicates** | **Allowed**                                  |

**Example:**

Python

```
shopping_list = ["apples", "bananas", "milk", "apples"]
print(shopping_list)
# Output: ['apples', 'bananas', 'milk', 'apples']

# Access by index
print(shopping_list[1])
# Output: bananas

# Mutability (changing an item)
shopping_list[2] = "cheese"
print(shopping_list)
# Output: ['apples', 'bananas', 'cheese', 'apples']
```



## Dictionaries (Mutable, Unordered, Key-Value)

A **dictionary** is an unordered, mutable collection of data that stores data in **key-value pairs**. Each **key** must be unique and immutable (like a string or a number), and it's used to look up its corresponding **value**.

| Feature        | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Syntax**     | Enclosed in curly braces `{}`, with a colon separating keys and values (`key: value`) |
| **Order**      | **Insertion-ordered** (since Python 3.7)                     |
| **Mutability** | **Mutable** (keys/values can be added, removed, or changed)  |
| **Indexing**   | Accessed by **Key**, not by numerical index                  |

**Example:**

Python

```
student_profile = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
print(student_profile)
# Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# Access by key
print(student_profile["major"])
# Output: Computer Science

# Mutability (adding a new key-value pair)
student_profile["gpa"] = 3.8
print(student_profile)
# Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'gpa': 3.8}
```



## Sets (Mutable, Unordered, Unique)

A **set** is an unordered, mutable collection of **unique** elements. Because sets are unordered, they **do not** support indexing, but they are highly efficient for operations involving membership testing and eliminating duplicates.

| Feature        | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Syntax**     | Enclosed in curly braces `{}`, or using the `set()` constructor |
| **Order**      | **Unordered** (items don't have a defined index)             |
| **Mutability** | **Mutable** (can add or remove items)                        |
| **Duplicates** | **Not Allowed** (automatically removes duplicates)           |

**Example:**

Python

```
prime_numbers = {2, 3, 5, 7, 11}
colors = {"red", "green", "blue", "red"}
print(colors)
# Output: {'blue', 'red', 'green'} (Order may vary, duplicates removed)

# Mutability (adding an item)
prime_numbers.add(13)
print(prime_numbers)
# Output: {2, 3, 5, 7, 11, 13}

# Using a set to find unique items in a list
data = [1, 2, 2, 3, 4, 4, 1]
unique_data = set(data)
print(unique_data)
# Output: {1, 2, 3, 4}
```



## Tuples (Immutable, Ordered, Indexed)

A **tuple** is an ordered, **immutable** (unchangeable) sequence of items. Like lists, tuples can contain duplicate elements and a mix of different data types. Because they are immutable, once a tuple is created, you cannot add, remove, or change its elements. Tuples are often used for data that shouldn't change, or as keys in dictionaries (which lists cannot be).

| Feature        | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| **Syntax**     | Enclosed in parentheses `()` (or sometimes no parentheses for a single item, but this can be ambiguous) |
| **Order**      | **Maintained** (items have a definite order)                 |
| **Mutability** | **Immutable** (cannot be changed after creation)             |
| **Duplicates** | **Allowed**                                                  |

**Example:**

Python

```
coordinates = (10.0, 20.5)
rgb_color = ("red", 255, 0, 0) # Common use for fixed sets of values
print(coordinates)
# Output: (10.0, 20.5)

# Access by index (like lists)
print(rgb_color[0])
# Output: red

# Immutability (this would cause an error if uncommented)
# coordinates[0] = 15.0 # TypeError: 'tuple' object does not support item assignment

# A common use case: returning multiple values from a function
def get_user_info():
    return "Alice", 30, "alice@example.com"

name, age, email = get_user_info()
print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 30
```



## References

- [**Python Data Structures**](https://docs.python.org/3/tutorial/datastructures.html)
  Part of the official Python Tutorial. Covers: lists, tuples, sets, and dictionaries.
- **W3Schools Python Collections**
  - [Python Lists](https://www.w3schools.com/python/python_lists.asp)
  - [Python Tuples](https://www.w3schools.com/python/python_tuples.asp)
  - [Python Sets](https://www.w3schools.com/python/python_sets.asp)
  - [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)



Note: This document was drafted using Gemini 2.5 Flash


---

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) Intro to AI Course Materials by [Brian Bird](https://profbird.dev), written in <time>2025</time>, are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 

---