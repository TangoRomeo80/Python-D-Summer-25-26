# This file contains the implementation of object-oriented programming concepts in Python.
# class Animal:
#     def make_sound(self):
#         print('Sound')

# a = Animal()
# a.make_sound()  # Output: Sound
class Student:
    # Parameterized constructor
    # def __init__(self, name, id, cgpa):
    #     # # Private attributes
    #     # self.__final_year = 2024
    #     # # Protected attributes
    #     # self._x = 10
    #     self.name = name
    #     self.id = id
    #     self.cgpa = cgpa

    # # Default constructor
    def __init__(self):
        self.name = ""
        self.id = 0
        self.cgpa = 0.0

    # Constructor with partial parameters
    # def __init__(self, name, id, cgpa=4.0):
    #     self.name = name
    #     self.id = id
    #     self.cgpa = cgpa

# s = Student('John Doe', 12345, 3.8)
# print(s.final_year)  # This will raise an AttributeError because final_year is private
# print(s._Student__final_year)
# s1 = Student('Alice', 1001, 3.9)
# s2 = Student('Bob', 1002)  # cgpa will default to 4.0
s3 = Student()
print(s3.__dict__)