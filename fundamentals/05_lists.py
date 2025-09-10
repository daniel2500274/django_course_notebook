list_numbers = [1, 2, 3, 4, 5]
list_letters = ["a", "b", "c", "d", "e"]
list_mixed = [1, "a", 2, "b", 3, "c"]

shopping_list = ["eggs", "milk", "bread", "butter"]
print(shopping_list)

# List Metods
shopping_list.append("cheese")  # Add an item to the end of the list
print(shopping_list)
shopping_list.remove("milk")  # Remove an item from the list
print(shopping_list)
shopping_list.pop()
print(shopping_list)  # Remove and return the last item
shopping_list.insert(1, "yogurt")  # Insert an item at a specific position
print(shopping_list)
print(shopping_list.index("bread"))  # Get the index of an item
print(shopping_list.count("eggs"))  # Count occurrences of an item
print(len(shopping_list))
print(shopping_list)