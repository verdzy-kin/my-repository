# # concatenation and interpolation (string operations in python)
# first_name="John"
# last_name="Ngalah"
# # concatenation
# full_names=first_name + last_name

# # interpolation

# print(f"my fullnames are {full_names}")
# ".................................."
# # .........

# laugh = "Ha" * 7
# # "hahaha"
# print(laugh)
# split() method



# ______________________________STRING SOLUTION___________

# Get a full name and format it properly
full_name = "jOhN dOe"
# Make it: "John Doe"
# Print first name and last name separately
# print("Correct solution is: " + full_name.title())

# full_name[0]=full_name[0].upper()
# full_name[3].lower()
# full_name[5].upper()

# print(f"Converted character: {get_j}  {get_n}  {get_d}")
# full_name[0]=get_j
# full_name[3]=get_n
# full_name[5]=get_d

print("Correct solution is: " + full_name)

# strings in python are immutable, we can change them

greetings="hello"
# we want to change from "hello"->"y"
print("My greetings: " + greetings[0:4])
# greetings[0]="y"
# print("Greetings here is: " + greetings)
# 1 convert our string to a python list
# 2. Use slicing and concatenation
# meaning starting now from index 1
# greetings="y" + greetings[1:]

# print("Greetings here is: " + greetings)

sentence = "Python is an amazing programming language"
# Count how many words
word_count=sentence.split(" ")
joined="".join(word_count)
word_count=len(word_count)
print(f"Word count is {joined}")
# Count how many characters (including spaces)
# Count how many times 'a' appears
# count_a=0
# for i in range(len(joined)): 
#     print(i)
#     if joined[i]=="a":
#         count_a+=1
        
# print(f"a appears : {count_a} times")
a_count=sentence.count("a")
print(f"a appears {a_count}")

