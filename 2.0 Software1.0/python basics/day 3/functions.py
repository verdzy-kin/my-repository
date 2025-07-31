# # #a functiion is a block of code which executes a particular task
# # def BMI_calculator(weight, height):
# #     # weight=float(input("enter weight: "))
# #     # height=float(input("Enter height: "))
# #     BMI = weight/(height*height)
# #     print(f"{BMI}kg/cm2")
# #     if BMI < 18:
# #         print("Underweight")
# #     elif BMI >18 and BMI < 25:
# #         print("Normal")
# #     elif BMI > 25 and BMI < 30:
# #         print("overweighed")
# #     else:
# #         print("Obese")

# # print(BMI_calculator())

# def areaofCircle(radius):
#     pi = 3.14159
#     area = pi * radius * radius
#     return area

# area1 = areaofCircle(9)
# area2 =areaofCircle(17)
# area3 = areaofCircle(28)

# print(f"Area of circle 1: {area1}")
# print(f"Area of circle 2: {area2}")
# print(f"Area of circle 3: {area3}")

# def greetings(name):
#     message = f"hello, {name}! Welcome to python!"
#     return message

# greet = greetings("Delsy")
# print(greet)



#FUNCTION EXERCISES
#EXERCISE 1
def createProfile(name, age, occupation, city):
    profile = f"Name: {name} \nAge: {age} \nOccupation: {occupation} \nCity: {city}"
    return profile
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# occupation = input("Enter occupation: ")
# city = input("Enter city: ")
print(createProfile('delsy', 31, 'Engineer', 'Yaounde'))

#EXERCISE 2
def gradeCalculator(mark):   
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
    return mark


print(gradeCalculator(95))
print(gradeCalculator(87))
print(gradeCalculator(83))


#EXERCISE 3
def calculateTotal(price, quantity, tax_rate=0.08):
    subtotal = price * quantity
    taxAmount = subtotal * tax_rate
    total = subtotal * taxAmount
    return total

total = calculateTotal(29.99, 3)
print(f"Total cost: ${total:.2f}")