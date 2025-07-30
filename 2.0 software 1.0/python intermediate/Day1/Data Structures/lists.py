########## DATA STRUCTURES ##############
# ##LISTS
# shopping_cart = ["apples", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5]
# mixed_items = ["Alice", 25, True, 3.24]
# empty_cart = []
# print(f"Shopping cart: {shopping_cart}\nNumbers: {numbers}\nMixed Items: {mixed_items}")

# ########## Accessing List Items ###########
# fruits = ["apple", "banana", "pineapple", "cherry", "mango", "blueberry"]
# #Accessing by index
# print(f"First fruit: {fruits[0]}\nSecond fruit: {fruits[1]}\nLast fruit: {fruits[-1]}\nSecond to last fruit: {fruits[-2]}")

# #Getting sliced portions of the list
# print(f"First 3 fruits: {fruits[0:3]}\nFrom 3rd to end: {fruits[2:]}\nFruits after every increment by 2(every second fruit): {fruits[::2]}")

# ## Modifying Lists: The grocery dilemma

# # Starting with a basic grocery list
# groceries = ["milk", "bread", "eggs"]
# print(f"Original list: {groceries}")

# #add single item to end of list
# groceries.append("supra")
# print(f"After adding supra: {groceries}")

# # Add multiple items
# groceries.extend(["cake,scotch egg"])
# print(f"After adding foods: {groceries}")

# # Changing items
# groceries[0] = "juice"
# print(f"After changing: {groceries}")

# # removing items
# groceries.remove("eggs")
# print(f"After removing: {groceries}")

# # groceries.po() - removes last item
# popped = groceries.pop(2)
# print(f"Popped item: {popped}")
# print(f"After popping: {groceries}")

## List Methods and Operations

# Sample list of test scores(integers)
test_scores = [85, 92, 78, 96, 88, 79, 94]

# Getting information about the list(max(), len(), min(), sum())
print(f"Number of scores: {len(test_scores)}")
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")
print(f"Average score: {sum(test_scores) / len(test_scores):.1f}")

# Checking if items exist
print(f"Is 85 in the list? {85 in test_scores}")
print(f"Is 100 in the list? {100 in test_scores}")

# Counting occurrences
grades = ["A", "B", "A", "C", "B", "A", "D"]
print(f"Number of A's: {grades.count('A')}")

# Finding the position of an item
print(f"Position of first 'B': {grades.index('B')}")

# Sorting (this changes the original list)
test_scores.sort()
print(f"Sorted scores: {test_scores}")

# Sorting in descending order
test_scores.sort(reverse=True)
print(f"Scores (highest to lowest): {test_scores}")

# Reversing the list
test_scores.reverse()
print(f"Reversed list: {test_scores}")