# def read_sample_file():
#     """demonstrate basic file reading-----
#     hvsiohiuvdn
#     """
#     file = open("sample.txt","r")
#     # print(f"here is the file I wanted to read_______ : {file}")
#     content = file.read()
#     print(f"here is the content of the file read: {content}")
#     file.close()
#     return content

# read_sample_file()

# ## Optimized Version
# def read_sample_file():
#     """"""
#     with open("sample.txt","r") as file:
#         content = file.read()
#         print(f"File content is: {content}")
#         return content
    
# read_sample_file()

# ## Handles errors
# def read_simple_file():
#     filename = "new_file.txt" # Of course file is not found and empty
#     try:
#         with open(filename, "r") as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         return "file not found."
    
# print(read_simple_file())

## Looping through file a line at a time

# def line_by_line():
#     filename = "sample.txt"
#     try:
#         with open(filename, "r") as file:
#             print("Reading file line by line: \n")
#             for i, line in enumerate(file):
#                 print(f"Line {i}: {line}")
#     except FileNotFoundError:
#         pass

# line_by_line()