# This file will contain function related codes
def function_name(parameters):
    # Function body
    pass
    # return value

# Without annotation
# def add(a, b):
#     return a + b

# With annotation
# def add(a: int, b: int) -> int:
#     return a + b

# print(add(5, 3))

3 # Without default parameter
# def greet(name: str) -> str:
#     return f"Hello, {name}!"

# With default parameter
# def  greet(name: str = "World") -> str:
#     return f"Hello, {name}!"

# print(greet("Alice"))
# print(greet())

# Keyword arguments
# def student_details(name: str, age: int, grade: str = "A") -> str:
#     return f"Student Name: {name}, Age: {age}, Grade: {grade}"

# print(student_details("John", 16, "B")) # Positional arguments
# print(student_details(age=15, name="Alice")) # Keyword arguments

# Scope of variables
# while True:
#     x = 10
#     if x > 5:
#         print("x is greater than 5")
#         print(x)
#         break
#     x -= 1
# print(x)

# def display() -> None:
#     message = "Hello, World!"
#     print(message)

# display()  # Output: Hello, World!
# print(message)  # This will raise a NameError since 'message' is not defined in this scope

# marks = [75, 40, 90, 60, 85]
# sorted_marks = sorted(marks)
# print(sorted_marks)

# students = ['Alice', 'Bob', 'Charlie', 'David']
# for index, student in enumerate(students):
#     print(f"Index: {index}, Student: {student}")