"""
Modules Python Introduction
In the world of programming, we care a lot about making code reusable. In most cases, we write code so that it can be reusable for ourselves. But sometimes we share code that’s helpful across a broad range of situations.

In this lesson, we’ll explore how to use tools other people have built in Python that are not included automatically for you when you install Python. Python allows us to package code into files or sets of files called modules.

A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

Usually, to use a module in a file, the basic syntax you need at the top of that file is:

from module_name import object_name

Often, a library will include a lot of code that you don’t need that may slow down your program or conflict with existing code. Because of this, it makes sense to only import what you need.

One common library that comes as part of the Python Standard Library is datetime. datetime helps you work with dates and times in Python.

Let’s get started by importing and using the datetime module. In this case, you’ll notice that datetime is both the name of the library and the name of the object that you are importing.
"""

from datetime import datetime

current_time = datetime.now()
print(current_time)

# Random modules

# 1. Create a variable random_list and set it equal to an empty list
# 2. Turn the empty list into a list comprehension that uses random.randint() to generate a random integer between 1 and 100 (inclusive) for each number in range(101).
# 3. Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument.
# 4. Print randomer_number out to see what number was picked!

import random

random_list = [random.randint(1, 100) for i in range(101)]

randomer_number = random.choice(random_list)

print(random_list)
print(randomer_number)
