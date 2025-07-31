
def style():
    print("_"*40)


# def num_error():
#     style()
#     userInput = int(input("Enter phone number: "))
#     print(f"user input is: {userInput}")

# def num_error():
#     try:
#         style()
#         userInput = int(input("Enter phone number: "))
#         print(f"user input is: {userInput}")
#     except ValueError:
#         print("make sure you're inputting a number")

    # try:
    # except :

# def Div_error():
#     try:
#         style()
#         firstnum=int(input("1st num: "))
#         secondnum=int(input("2nd num: "))
#         return firstnum/secondnum
#     except ZeroDivisionError:
#         print("cant divide by 0")

def dictError(data):
    try:            
        color = data["color"]
        print(f"color is: {color}")
        pass
    except KeyError:
        print("key not found")

data = {"name": "Delsy",
        "age": 18,
        "fav meal": "rice"
        }
dictError(data)
# Div_error()
# num_error()