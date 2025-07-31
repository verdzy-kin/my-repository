# shoppingCart = ["apples", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5, 6]
# mixedItems = ['alice', 25, True, 3.14]
# emptyCart = []

# print(f"shopping cart: {shoppingCart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixedItems}")

# fruits = ["apples", "orange", "pineapple", "watermelon", "grapes", "lorem2", "shdfds", "sdfgnb", "sdfsde"]
# print(f"first fruit: {fruits[0]}")
# print(f"2nd fruit: {fruits[1]}")
# print(f"last fruit: {fruits[-1]}")
# print(f"1st 3 fruits: {fruits[0:3]}")
# print(f"from 2nd to the end: {fruits[1:]}")
# print(f"Every second fruit: {fruits[::2]}")


groceries = ["milk", "bread", "eggs"]
print(f"Original list: {groceries}")

# Adding single items (like adding items to your cart)
groceries.append("cheese")
print(f"After adding cheese: {groceries}")

# Adding multiple items at once
groceries.extend(["apples", "bananas"])
print(f"After adding fruits: {groceries}")

# Inserting an item at a specific position
groceries.insert(1, "yogurt")  # Insert at index 1
print(f"After inserting yogurt: {groceries}")

# Changing an existing item
groceries[0] = "almond milk"  # Change milk to almond milk
print(f"After changing milk: {groceries}")

# Removing items
groceries.remove("bread")  # Remove by value
print(f"After removing bread: {groceries}")

removed_item = groceries.pop()  # Remove and return last item
print(f"Removed item: {removed_item}")
print(f"After popping: {groceries}")

specific_item = groceries.pop(1)  # Remove and return item at index 1
print(f"Removed item at index 1: {specific_item}")
print(f"Final list: {groceries}")
