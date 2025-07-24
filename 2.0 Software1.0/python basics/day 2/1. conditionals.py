# import random

# # 🖼️ Array of ASCII art diagrams
# ascii_art_diagrams = [
#     r"""
#      /\_/\
#     ( o.o )
#      > ^ <
#     """,

#     r"""
#      _______
#     |       |
#     |       O
#     |      /|\
#     |      / \
#     |
#     =========
#     """,

#     r"""
#     _______
#    /       \
#   |  (• ◡•)  |
#    \_______/
#     """,

#     r"""
#      __
#     /  \
#    |    |
#    |____|
#   /      \
#  /________\
#     """
# ]

# # 📝 Array of creative writing prompts
# story_prompts = [
#     "Write a story about a robot who wants to be human.",
#     "Describe a world where plants can talk to people.",
#     "Create a mystery involving a time-traveling detective.",
#     "Tell a bedtime story set on a spaceship.",
#     "Imagine a dragon who’s afraid of fire.",
#     "Write about a kid who finds a magical notebook.",
#     "Narrate a short poem about loneliness and the moon.",
#     "Describe an ancient civilization powered by sound."
# ]



#conditionals arelike the decision making brains of your program

# age = int(input("enter your age"))
# if age > 18:
#     print(" Welcome\n you can vote....")
# else:
#     print("wait till your 18")


# if age > 16:
#     print("You  can play in the basketball team")
# else:
#     print("wait till you're 16")

print("__"*50)
print("school grading system....")
mark = float(input("Enter marks:  "))
if  mark >= 80:
    print("A-grade")
elif mark >= 70:
    print("B+ grade")
elif mark >= 60:
    print("B-grade")
elif mark >= 50:
    print("C-grade")
elif mark > 40:
    print("D-grade")
elif mark < 40:
    print("fail")