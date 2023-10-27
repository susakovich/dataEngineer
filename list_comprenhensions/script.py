# Practice lists comprenhension

nums = [10, 23, 4, -5, 112, 38, -89]
doubles_nums = [num * 2 for num in nums]
print(doubles_nums)

doubled_negative_nums = [num * 2 for num in nums if num < 0]
print(doubled_negative_nums)

double_negative_triple_positive_nums = [num * 2 if num < 0 else num * 3 for num in nums]
print(double_negative_triple_positive_nums)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)


"""
1.
Create a list called single_digits that consists of the numbers 0-9 (inclusive).

2. Create a for loop that goes through single_digits and prints out each one.

3. Before the loop, create a list called squares. Assign it to be an empty list to begin with.

4. Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

5. After the for loop, print out squares.

6. Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

7. Print cubes.
"""

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for digit in single_digits:
    squared = digit**2
    squares.append(squared)
    print(digit)
print(squares)

cubes = [num**3 for num in single_digits]
print(cubes)
