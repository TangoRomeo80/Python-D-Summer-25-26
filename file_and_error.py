# # # This file contains file and error handling example codes
# # with open('example.txt', 'w') as f:
# #     f.write('Hello, World!\n')
# #     f.write('This is written as a new line.\n')

# # with open('example.txt', 'r') as f:
# #     content = f.read()
# #     print(content)

# # with open('example.txt', 'a') as f:
# #     f.write('This line is appended to the file.\n')

# # filename = 'non_existent_file.txt'
# filename = 'example.txt'  # Change this to a non-existent file to test error handling
# try:
#     with open(filename, 'r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' does not exist.")
# except PermissionError:
#     print(f"Error: You do not have permission to read the file '{filename}'.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


