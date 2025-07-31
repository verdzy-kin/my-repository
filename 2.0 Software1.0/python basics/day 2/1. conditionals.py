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

# print("__"*50)
# print("school grading system....")
# mark = float(input("Enter marks:  "))
# if  mark >= 80:
#     print("A-grade")
# elif mark >= 70:
#     print("B+ grade")
# elif mark >= 60:
#     print("B-grade")
# elif mark >= 50:
#     print("C-grade")
# elif mark > 40:
#     print("D-grade")
# elif mark < 40:
#     print("fail")
# else:
#     print("sorry")


#a simple calculator

# first_number=float(input("Enter first number:  "))
# second_number=float(input("Enter second number:  "))
# operator=input("Enter operator:  ")
# result = 0

# if operator=="+":
#     print(first_number + second_number)
# elif operator=="-":
#     print(first_number - second_number)
# elif operator=="*":
#     print(first_number * second_number)
# elif operator=="/":
#     if second_number==0:
#         print("can't divide by 0")
#     else:
#         print(first_number / second_number)    
# else:
#     print("Not an operator")


#Leapyear exercise 
year=int(input("enter year: "))
if year%4!=0 and year%100!=0 and year%400!=0:
    print("not a leap year")    
else:
    print("leap year")

# Leap year exercise
year = int(input("Enter year: "))
if year%4!= 0:
    if year%100!= 0:
        if year%400!= 0:
            print("Not a leap year")
else:
    print("Leap year")