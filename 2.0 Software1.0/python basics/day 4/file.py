# # The basic pattern for reading files
# def read_simple_file():
#     """Demonstrate basic file reading.
#     iohohihkjhkgfjfgnvhmnvcvhmbcdythdmh
#     """
#     # Open the file (like opening a filing cabinet drawer)
#     file = open("sample.txt", "r")  # "r" stands for "read mode" "w" stands for write mode
#     # Read the contents (like reading the document)
#     content = file.read()
#     # Close the file (like putting the document back and closing the drawer)
#     print(content)
#     file.close()
#     return content

# read_simple_file()

# #Alternative to read files without having to manually close

# def read_simple_text():
#     """"""
#     with open("sample.txt","r") as file:
#         content = file.read()
#         print(f"content is {content}")
#         return content
# read_simple_text()

# # A safer way using 'with' statement (automatic cleanup)
# def read_file_safely(filename):
#     """Read a file with automatic cleanup."""
#     try:
#         with open(filename, "r") as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         return "File not found!"

# Reading different ways
# def demonstrate_reading_methods():
#     """Show different ways to read file content."""
#     filename = "example.txt"

#     with open(filename, "r") as file:
#         # Method 1: Read entire file at once
#         all_content = file.read()
#         print("Entire file:", all_content[:50] + "...")  # Show first 50 characters

#     with open(filename, "r") as file:
#         # Method 2: Read line by line
#         print("Reading line by line:")
#         for line_number, line in enumerate(file, 1):
#             print(f"Line {line_number}: {line.strip()}")  # strip() removes newline characters

#     with open(filename, "r") as file:
#         # Method 3: Read all lines into a list
#         all_lines = file.readlines()
#         print(f"Total lines: {len(all_lines)}")

# demonstrate_reading_methods()

# def line_by_line():
#     filename = "sample.txt"
#     try:
#         with open(filename, "r") as file:
#             print("\n\nreading line by line")
#             for i, line in enumerate(file, 1):
#                 print(f"\n\nLine {i}:{line.strip()}")
#     except FileNotFoundError:
#         pass
# line_by_line()


#WRITING FILES IN PYTHON
def Records_file():
    from datetime import datetime
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("./record.txt", "w") as file:
        file.write("\n\t\t\t****RECORDS BOOK****\n")
    # content = input("What did u learn today? ")
        with open("./record.txt", "w") as file: 
            while True:      
                print(f"TODAY'S DATE: {currentTime}\n     NOTE:")
                text = input("")
                if text.strip().lower() == "exit":
                    break
                else:
                    file.write(f"TODAY'S DATE: {currentTime}")
                    file.write("NOTE: \n")
                    file.write(text + "\n")
Records_file()
    