# Creating sets - like building unique collections
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green", "yellow"}
mixed_set = {1, "hello", 3.14, True}

# Creating sets from lists (removes duplicates automatically)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers_from_list = set(numbers_with_duplicates)

# Empty set (note: {} creates an empty dictionary, not set)
empty_set = set()

print(f"Unique numbers: {unique_numbers}")
print(f"Colors: {colors}")
print(f"From list with duplicates: {unique_numbers_from_list}")
print(f"Empty set: {empty_set}")


python_students = {"Charlie", "Eve", "Frank"}
java_students = {"Charlie", "Davis", "Claudia", "Joan"}
javascript_students = {"Charlie", "Diana", "Eve", "Grace"}

# Union - students taking ANY programming course
all_programming_students = python_students | java_students | javascript_students
print(f"All programming students: {all_programming_students}")

# Intersection - students taking BOTH Python AND Java
python_and_java = python_students & java_students
print(f"Students taking both Python and Java: {python_and_java}")

# Difference - students taking Python but NOT Java
python_only = python_students - java_students
print(f"Students taking Python but not Java: {python_only}")

# Symmetric difference - students taking Python OR Java but not both
python_xor_java = python_students ^ java_students
print(f"Students taking Python or Java but not both: {python_xor_java}")


# Starting with a basic set of skills
my_skills = {"Python", "JavaScript", "HTML"}
print(f"Initial skills: {my_skills}")

# Adding single skills
my_skills.add("CSS")
my_skills.add("React")
print(f"After learning CSS and React: {my_skills}")

# Adding multiple skills at once
new_skills = {"Node.js", "MongoDB", "Docker"}
my_skills.update(new_skills)
print(f"After bootcamp: {my_skills}")

# Removing skills (maybe you forgot some!)
my_skills.remove("HTML")  # Raises error if not found
print(f"After forgetting HTML: {my_skills}")

# Safer removal (won't raise error if not found)
my_skills.discard("PHP")  # Won't cause error even though PHP isn't in the set
print(f"After trying to remove PHP: {my_skills}")

# Removing and returning an arbitrary element
removed_skill = my_skills.pop()
print(f"Randomly removed skill: {removed_skill}")
print(f"Remaining skills: {my_skills}")

# Email subscription management
# def manage_email_subscriptions():
#     """Manage different email subscription lists."""
#     newsletter_subscribers = {"alice@email.com", "bob@email.com", "charlie@email.com"}
#     promotion_subscribers = {"bob@email.com", "diana@email.com", "eve@email.com"}

#     # Find subscribers who get both newsletters and promotions
#     both_subscriptions = newsletter_subscribers & promotion_subscribers
#     print(f"Subscribers getting both: {both_subscriptions}")

#     # Find all unique subscribers
#     all_subscribers = newsletter_subscribers | promotion_subscribers
#     print(f"All subscribers: {all_subscribers}")

#     # Find newsletter-only subscribers
#     newsletter_only = newsletter_subscribers - promotion_subscribers
#     print(f"Newsletter only: {newsletter_only}")

#     return all_subscribers

# # Word uniqueness checker
# def find_unique_words(text1, text2):
#     """Find unique words in two texts."""
#     # Convert to lowercase and split into words
#     words1 = set(text1.lower().split())
#     words2 = set(text2.lower().split())

#     # Clean up punctuation

#     words2 = {word.strip(".,!?;:") for word in words2}

#     # Find common words
#     common_words = words1 & words2

#     # Find unique words in each text
#     unique_to_text1 = words1 - words2
#     unique_to_text2 = words2 - words1

#     return {
#         "common": common_words,
#         "unique_to_first": unique_to_text1,
#         "unique_to_second": unique_to_text2
#     }

# # Test the word analyzer
# text1 = "Python is a great programming language for beginners"
# text2 = "Java is also a popular programming language for developers"

# word_analysis = find_unique_words(text1, text2)
# print("Word Analysis:")
# print(f"Common words: {word_analysis['common']}")
# print(f"Unique to first text: {word_analysis['unique_to_first']}")
# print(f"Unique to second text: {word_analysis['unique_to_second']}")

# # Inventory system using sets
# def track_inventory_categories():
#     """Track different categories of products in inventory."""
#     electronics = {"laptop", "phone", "tablet", "headphones"}
#     discounted_items = {"laptop", "book", "shirt", "headphones"}
#     popular_items = {"phone", "book", "laptop", "shoes"}

#     # Find electronics that are on discount
#     discounted_electronics = electronics & discounted_items
#     print(f"Discounted electronics: {discounted_electronics}")

#     # Find popular electronics
#     popular_electronics = electronics & popular_items
#     print(f"Popular electronics: {popular_electronics}")

#     # Find all product categories
#     all_products = electronics | discounted_items | popular_items
#     print(f"All products: {all_products}")


#     # Find all product categories
#     all_products = electronics | discounted_items | popular_items
#     print(f"All products: {all_products}")

# manage_email_subscriptions()
# track_inventory_categories()
# Working with Multiple Data Structures
# Combining Different Data Structures
# In real-world programming, you often need to combine different data structures to solve complex problems. Think of this like using different tools from your toolbox together to build something sophisticated.

# # Complex student management system
# class_roster = {
#     "CS101": {
#         "course_name": "Introduction to Programming",
#         "students": ["Alice", "Bob", "Charlie"],
#         "assignments": [
#             {"name": "Hello World", "due_date": "2024-02-15", "points": 10},
#             {"name": "Variables and Types", "due_date": "2024-02-22", "points": 25}
#         ],
#         "grades": {
#             "Alice": [10, 23],
#             "Bob": [8, 22],
#             "Charlie": [10, 25]
#         }
#     },
#     "CS102": {
#         "course_name": "Data Structures",
#         "students": ["Alice", "Diana", "Eve"],
#         "assignments": [
#             {"name": "Arrays", "due_date": "2024-02-20", "points": 30},
#             {"name": "Linked Lists", "due_date": "2024-02-27", "points": 35}
#         ],
#         "grades": {
#             "Alice": [28, 33],
#             "Diana": [30, 35],
#             "Eve": [25, 30]
#         }
#     }
# }

# def calculate_student_average(course_code, student_name):
#     """Calculate average grade for a student in a specific course."""
#     if course_code in class_roster and student_name in class_roster[course_code]["grades"]:
#         grades = class_roster[course_code]["grades"][student_name]
#         total_points = sum(grades)

#         # Calculate total possible points
#         assignments = class_roster[course_code]["assignments"]
#         total_possible = sum(assignment["points"] for assignment in assignments)

#         percentage = (total_points / total_possible) * 100
#         return percentage
#     else:
#         return None

# def find_common_students(*course_codes):
#     """Find students enrolled in multiple courses."""
#     if not course_codes:
#         return set()

#     # Start with students from first course
#     common_students = set(class_roster[course_codes[0]]["students"])

#     # Find intersection with other courses
#     for course_code in course_codes[1:]:
#         course_students = set(class_roster[course_code]["students"])
#         common_students &= course_students

#     return common_students

# # Using the system
# print("Alice's average in CS101:", f"{calculate_student_average('CS101', 'Alice'):.1f}%")
# print("Students in both CS101 and CS102:", find_common_students("CS101", "CS102"))

# # Recipe management system combining all data structures
# recipe_database = {
#     "Pancakes": {
#         "ingredients": [
#             ("flour", 2, "cups"),
#             ("milk", 1.5, "cups"),
#             ("eggs", 2, "pieces"),
#             ("sugar", 2, "tablespoons")
#         ],
#         "instructions": [
#             "Mix dry ingredients in a bowl",
#             "Combine wet ingredients separately",
#             "Gradually add wet to dry ingredients",
#             "Cook on griddle until golden"
#         ],
#         "prep_time": 10,
#         "cook_time": 15,
#         "servings": 4,
#         "dietary_tags": {"vegetarian"}
#     },
#     "Chicken Stir Fry": {
#         "ingredients": [
#             ("chicken breast", 1, "pound"),
#             ("broccoli", 2, "cups"),
#             ("soy sauce", 3, "tablespoons"),
#             ("garlic", 2, "cloves")
#         ],
#         "instructions": [
#             "Cut chicken into bite-sized pieces",
#             "Heat oil in wok or large pan",
#             "Cook chicken until done",
#             "Add vegetables and sauce"
#         ],
#         "prep_time": 15,
#         "cook_time": 12,
#         "servings": 3,
#         "dietary_tags": {"gluten-free", "high-protein"}
#     }
# }

# def find_recipes_by_time(max_total_time):
#     """Find recipes that can be made within a time limit."""
#     suitable_recipes = []

#     for recipe_name, recipe_info in recipe_database.items():
#         total_time = recipe_info["prep_time"] + recipe_info["cook_time"]
#         if total_time <= max_total_time:
#             suitable_recipes.append((recipe_name, total_time))

#     # Sort by total time
#     suitable_recipes.sort(key=lambda x: x[1])
#     return suitable_recipes

# def get_shopping_list(recipe_names):
#     """Generate shopping list for multiple recipes."""
#     shopping_list = {}

#     for recipe_name in recipe_names:
#         if recipe_name in recipe_database:
#             for ingredient, amount, unit in recipe_database[recipe_name]["ingredients"]:
#                 if ingredient in shopping_list:
#                     # Simple aggregation (assumes same units)
#                     shopping_list[ingredient] += amount
#                 else:
#                     shopping_list[ingredient] = amount

#     return shopping_list

# # Using the recipe system
# quick_recipes = find_recipes_by_time(30)
# print("Recipes under 30 minutes:")
# for recipe, time in quick_recipes:
#     print(f"- {recipe}: {time} minutes")

# shopping_list = get_shopping_list(["Pancakes", "Chicken Stir Fry"])
# print("\nShopping list:")
# for ingredient, amount in shopping_list.items():
#     print(f"- {ingredient}: {amount}")
# Data Structure Selection Guide
# Understanding when to use each data structure is crucial for efficient programming:


# # Complex student management system
# class_roster = {
#     "CS101": {
#         "course_name": "Introduction to Programming",
#         "students": ["Alice", "Bob", "Charlie"],
#         "assignments": [
#             {"name": "Hello World", "due_date": "2024-02-15", "points": 10},
#             {"name": "Variables and Types", "due_date": "2024-02-22", "points": 25}
#         ],
#         "grades": {
#             "Alice": [10, 23],
#             "Bob": [8, 22],
#             "Charlie": [10, 25]
#         }
#     },
#     "CS102": {
#         "course_name": "Data Structures",
#         "students": ["Alice", "Diana", "Eve"],
#         "assignments": [
#             {"name": "Arrays", "due_date": "2024-02-20", "points": 30},
#             {"name": "Linked Lists", "due_date": "2024-02-27", "points": 35}
#         ],
#         "grades": {
#             "Alice": [28, 33],
#             "Diana": [30, 35],
#             "Eve": [25, 30]
#         }
#     }
# }

# def calculate_student_average(course_code, student_name):
#     """Calculate average grade for a student in a specific course."""
#     if course_code in class_roster and student_name in class_roster[course_code]["grades"]:
#         grades = class_roster[course_code]["grades"][student_name]
#         total_points = sum(grades)
#         # Calculate total possible points
#         assignments = class_roster[course_code]["assignments"]
#         total_possible = sum(assignment["points"] for assignment in assignments)
#         percentage = (total_points / total_possible) * 100
#         return percentage
#     else:
#         return None

# def find_common_students(*course_codes):
#     """Find students enrolled in multiple courses."""
#     if not course_codes:
#         return set()

#     # Start with students from first course
#     common_students = set(class_roster[course_codes[0]]["students"])

#     # Find intersection with other courses
#     for course_code in course_codes[1:]:
#         course_students = set(class_roster[course_code]["students"])
#         common_students &= course_students

#     return common_students

# # Using the system
# print("Alice's average in CS101:", f"{calculate_student_average('CS101', 'Alice'):.1f}%")
# print("Students in both CS101 and CS102:", find_common_students("CS101", "CS102"))

# # Recipe management system combining all data structures
# recipe_database = {
#     "Pancakes": {
#         "ingredients": [
#             ("flour", 2, "cups"),
#             ("milk", 1.5, "cups"),
#             ("eggs", 2, "pieces"),
#             ("sugar", 2, "tablespoons")
#         ],
#         "instructions": [
#             "Mix dry ingredients in a bowl",
#             "Combine wet ingredients separately",
#             "Gradually add wet to dry ingredients",
#             "Cook on griddle until golden"
#         ],
#         "prep_time": 10,
#         "cook_time": 15,
#         "servings": 4,
#         "dietary_tags": {"vegetarian"}
#     },
#     "Chicken Stir Fry": {
#         "ingredients": [
#             ("chicken breast", 1, "pound"),
#             ("broccoli", 2, "cups"),
#             ("soy sauce", 3, "tablespoons"),
#             ("garlic", 2, "cloves")
#         ],
#         "instructions": [
#             "Cut chicken into bite-sized pieces",
#             "Heat oil in wok or large pan",
#             "Cook chicken until done",
#             "Add vegetables and sauce"
#         ],
#         "prep_time": 15,
#         "cook_time": 12,
#         "servings": 3,
#         "dietary_tags": {"gluten-free", "high-protein"}
#     }
# }

# def find_recipes_by_time(max_total_time):
#     """Find recipes that can be made within a time limit."""
#     suitable_recipes = []

#     for recipe_name, recipe_info in recipe_database.items():
#         total_time = recipe_info["prep_time"] + recipe_info["cook_time"]
#         if total_time <= max_total_time:
#             suitable_recipes.append((recipe_name, total_time))

#     # Sort by total time
#     suitable_recipes.sort(key=lambda x: x[1])
#     return suitable_recipes

# def get_shopping_list(recipe_names):
#     """Generate shopping list for multiple recipes."""
#     shopping_list = {}

#     for recipe_name in recipe_names:
#         if recipe_name in recipe_database:
#             for ingredient, amount, unit in recipe_database[recipe_name]["ingredients"]:
#                 if ingredient in shopping_list:
#                     # Simple aggregation (assumes same units)
#                     shopping_list[ingredient] += amount
#                 else:
#                     shopping_list[ingredient] = amount

#     return shopping_list

# # Using the recipe system
# quick_recipes = find_recipes_by_time(30)
# print("Recipes under 30 minutes:")
# for recipe, time in quick_recipes:
#     print(f"- {recipe}: {time} minutes")

# shopping_list = get_shopping_list(["Pancakes", "Chicken Stir Fry"])
# print("\nShopping list:")
# for ingredient, amount in shopping_list.items():
#     print(f"- {ingredient}: {amount}")

#     return shopping_list

# # Using the recipe system
# quick_recipes = find_recipes_by_time(30)
# print("Recipes under 30 minutes:")
# for recipe, time in quick_recipes:
#     print(f"- {recipe}: {time} minutes")

# shopping_list = get_shopping_list(["Pancakes", "Chicken Stir Fry"])
# print("\nShopping list:")
# for ingredient, amount in shopping_list.items():
#     print(f"- {ingredient}: {amount}")
# Data Structure Selection Guide
# Understanding when to use each data structure is crucial for efficient programming:

# # Practical examples of choosing the right data structure

# # Use LIST when:
# # - You need ordered data
# # - You need to access items by position
# # - You need to modify the collection frequently
# shopping_cart_items = ["apple", "bread", "milk", "eggs"]  # Order matters for checkout

# # Use DICTIONARY when:
# # - You need fast lookups by key
# # - You're storing related attributes
# # - You need to map one thing to another
# student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}  # Fast grade lookups

# # Use TUPLE when:
# # - Data shouldn't change
# # - You need to return multiple values from a function
# # - You're representing fixed records
# coordinates = (10, 20)  # Point coordinates shouldn't change arbitrarily

# # Use SET when:
# # - You need unique items only
# # - You need to find common or different items between groups
# # - You need fast membership testing
# unique_visitors = {"user1", "user2", "user3"}  # No duplicate visitors

# def demonstrate_data_structure_choice():
#     """Show practical examples of choosing the right data structure."""

#     # Scenario 1: Event planning
#     print("Event Planning System:")

#     # Guest list (order matters for seating)
#     guest_list = ["Alice", "Bob", "Charlie", "Diana"]

#     # RSVP responses (fast lookup by name)
#     rsvp_responses = {
#         "Alice": "Yes",
#         "Bob": "No", 
#         "Charlie": "Yes",
#         "Diana": "Maybe"
#     }

#     # Dietary restrictions (unique items only)
#     dietary_restrictions = {"vegetarian", "gluten-free", "vegan"}

#     # Event details (immutable record)
#     event_details = ("Wedding Reception", "2024-06-15", "Grand Ballroom")

#     print(f"Event: {event_details[0]} on {event_details[1]}")
#     print(f"Confirmed guests: {[guest for guest in guest_list if rsvp_responses.get(guest) == 'Yes']}")
#     print(f"Dietary restrictions to consider: {dietary_restrictions}")