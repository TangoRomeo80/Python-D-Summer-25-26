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

