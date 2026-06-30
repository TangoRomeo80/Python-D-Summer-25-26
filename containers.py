# This file contains codes related to different containers in python

# List
# Use a list when:
# 1. Order matters
# 2. Values may change
# 3. Duplicate values can be there
# 4. You want to use indexing and/or slicing
# marks = []
# marks = [90, 80, 70, 60, 50]
# mixed = [10, 'Hello', 3.14, True]
students = ['Alice', 'Bob', 'Charlie', 'David']
# print(students)
# print(students[0])
# Negative indexing starts from the end
# print(students[-1])  # Output: David
# Slicing
# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:4])  # Output: [20, 30, 40]
# print(numbers[:3])   # Output: [10, 20, 30]
# print(numbers[3:])   # Output: [40, 50, 60]
# print(numbers[::2])  # Output: [10, 30, 50]
# print(numbers[::-1]) # Output: [60, 50, 40, 30, 20, 10]
# print(numbers[-2:-4:-1])
# print(numbers[-2:-4:1])
# numbers.append(70)  # Adds 70 at the end of the list
# print(numbers)  # Output: [10, 20, 30, 40, 50, 60, 70]
#insert() adds an item at specific index
# numbers.insert(2, 25)  # Inserts 25 at index 2
# print(numbers)  # Output: [10, 20, 25, 30, 40, 50, 60]
# remove() removes the matching value
# numbers.remove(20)
# print(numbers)  # Output: [10, 20, 30, 40, 50, 60]
# Removing a value using index
# del numbers[1]  # Removes the value at index 1 (20)
# print(numbers)  # Output: [10, 30, 40, 50, 60]
# Pop removes and returns an element
# popped_value = numbers.pop()  # Removes and returns the last element (60)
# popped = numbers.pop(2)  # Removes and returns the last element (60)
# print(popped)  # Output: 60

# print(80 in numbers)
# squares = []
# for x in range(1, 6):
#     squares.append(x**2)
# print(squares)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # Output: [1, 4, 9, 16, 25]
# numbers = [10, 21, 33, 40, 50]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

# Use tuples when 
# 1. Order matters
# 2. Values should not change
# 3. You want to represent fixed records
# 4. You need sequence for dictionary keys or sets
# point = (10, 20)
# student = ('Alice', 20, 'A')
# x = [10]
# y = (10)
# print(type(x))  # Output: <class 'list'>
# print(type(y))  # Output: <class 'int'>
# y = (10,)
# print(type(y))
# a, b = (10, 20) # Tuple unpacking
# print(a)  # Output: 10
# print(b)  # Output: 20

# a, b = 10, 20
# print(a)
# print(b)

# Function returns multiple values as a tuple
# def caluculate(a: int, b: int) -> tuple:
#     sum_result = a + b
#     product_result = a * b
#     return sum_result, product_result

# Modifying mutable objects in an immutable object
# data = ([10, 20], [30, 40])
# data[1].append(50)
# print(data)

# Use set when:
# 1. Duplicate values should not exist
# 2. Order does not matter
# 3. Mathematical set operations are needed
# 4. Fast membership check is required

unique_numbers = {1, 2, 3, 4, 5}
# unique_ids = {} # This will not declare a set, it will declare a dictionary. To declare an empty set, use set()
# empty_set = set()  # Correct way to declare an empty set
# marks = [80, 85, 80, 91, 92, 92, 100]
# unique_marks = set(marks)
# print(unique_marks)
unique_numbers.add(6)  # Adds 6 to the set
# print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}
# unique_numbers.remove(10)  # Removes 3 from the set
# unique_numbers.discard(10)  # Removes 3 from the set if it exists, does nothing if it doesn't
# print(unique_numbers)  # Output: {1, 2, 4, 5, 6}
# print(7 in unique_numbers)  # Output: False

# ds_students = {'Alice', 'Bob', 'Charlie', 'David'}
# club_members = {'Charlie', 'David', 'Eve', 'Frank'}

# print(ds_students.union(club_members))  # Union of two sets
# print(ds_students | club_members)  # Union of two sets using | operator
# print(ds_students.intersection(club_members))  # Intersection of two sets
# print(ds_students & club_members)  # Intersection of two sets using & operator
# print(ds_students.difference(club_members))  # Difference of two sets
# print(club_members - ds_students)  # Difference of two sets using - operator
# print(ds_students.symmetric_difference(club_members))  # Symmetric difference of two sets
# print(ds_students ^ club_members)  # Symmetric difference of two sets using ^ operator

# Set conatining immutable objects
# mixed_set = {1, 2, (3, 4), 'Hello'}
# print(mixed_set)
# Set containing mutable objects will raise an error
# mutable_set = {1, 2, [3, 4], 'Hello'}  # This will raise a TypeError
# print(mutable_set)

# Use a dictionary when:
# 1. You want to associate keys with values
# 2. You want fast lookups by key
# 3. Data is supposed to have labels or attributes
# 4. You need to represent structured information

test = {} # This will declare a dictionary, not a set. To declare an empty set, use set()
student = {
    "id": 1,
    "name": "Alice",
    "age": 20,
    "department": "Computer Science",
}
# print(student["id"])
# print(student.get("name", "Not found"))  # Output: Alice
# student["cgpa"] = 3.8  # Adds a new key-value pair
# student["age"] = 21  # Updates the value for the key "age"
# print(student)
# Removing with pop() method
# student.pop('department')  # Removes the key "department" and its value
# print(student)
# for key in student:
#     print(key, ":", student[key])
# for key,value in student.items():
#     print(key, ":", value)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()  # New line after each row

# students = [
#     {"id": 1, "name": "Alice", "age": 20},
#     {"id": 2, "name": "Bob", "age": 22},
#     {"id": 3, "name": "Charlie", "age": 21}
# ]
# for student in students:
#     print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
