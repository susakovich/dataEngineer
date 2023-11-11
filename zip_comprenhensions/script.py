"""
Student names and heights, combine them using zip and dict comprenhensions
"""

names = ["Jenny", "Alice", "Bob", "Neo"]
heights = [89, 71, 67, 97]

students = {key: value for key, value in zip(names, heights)}
print(students)

# Another example

drinks = ["espresso", "chai", "machiatto", "drip"]
caffeine = [64, 40, 35, 120]
zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)
