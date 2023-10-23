"""
1. Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.

Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

First, how many items are in the warehouse?

Save the answer to a variable called inventory_len.

2. Select the first element in inventory. Save it to a variable called first.

3. Select the last element from inventory. Save it to a variable called last.

4. Select items from the inventory starting at index 2 and up to, but not including, index 6.

Save your answer to a variable called inventory_2_6.

5. Select the first 3 items of inventory. Save it to a variable called first_3.

6. How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.

7. Remove the 5th element in the inventory. Save the value to a variable called removed_item.

8. There was a new item added to our inventory called "19th Century Bed Frame".

Use the .insert() method to place the new item as the 11th element in our inventory.

9. Sort inventory using the .sort() method or the sorted() function.

Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().

Print inventory to see the result.
"""

inventory = [
    "twin bed",
    "twin bed",
    "headboard",
    "queen bed",
    "king bed",
    "dresser",
    "dresser",
    "table",
    "table",
    "nightstand",
    "nightstand",
    "king bed",
    "king bed",
    "twin bed",
    "twin bed",
    "sheets",
    "sheets",
    "pillow",
    "pillow",
]

inventory = [
    "twin bed",
    "twin bed",
    "headboard",
    "queen bed",
    "king bed",
    "dresser",
    "dresser",
    "table",
    "table",
    "nightstand",
    "nightstand",
    "king bed",
    "king bed",
    "twin bed",
    "twin bed",
    "sheets",
    "sheets",
    "pillow",
    "pillow",
]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
print(inventory)
