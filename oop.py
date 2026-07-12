# # This file contains the implementation of object-oriented programming concepts in Python.
# # class Animal:
# #     def make_sound(self):
# #         print('Sound')

# # a = Animal()
# # a.make_sound()  # Output: Sound
# class Student:
#     # Parameterized constructor
#     # def __init__(self, name, id, cgpa):
#     #     # # Private attributes
#     #     # self.__final_year = 2024
#     #     # # Protected attributes
#     #     # self._x = 10
#     #     self.name = name
#     #     self.id = id
#     #     self.cgpa = cgpa

#     # # Default constructor
#     def __init__(self):
#         self.name = ""
#         self.id = 0
#         self.cgpa = 0.0

#     # Constructor with partial parameters
#     # def __init__(self, name, id, cgpa=4.0):
#     #     self.name = name
#     #     self.id = id
#     #     self.cgpa = cgpa

# # s = Student('John Doe', 12345, 3.8)
# # print(s.final_year)  # This will raise an AttributeError because final_year is private
# # print(s._Student__final_year)
# # s1 = Student('Alice', 1001, 3.9)
# # s2 = Student('Bob', 1002)  # cgpa will default to 4.0
# s3 = Student()
# print(s3.__dict__)

# class Student:
#     # Class-level/Static variable
#     university = "AIUB"

#     def __init__(self, name, id, cgpa):
#         # These are all instance variables
#         self.name = name
#         self.id = id
#         self.cgpa = cgpa

#     # Class method to change the university for all instances
#     @classmethod
#     def change_university(cls, new_university):
#         cls.university = new_university

#     # Instance method
#     def display_info(self):
#         print(f"Name: {self.name}, ID: {self.id}, CGPA: {self.cgpa}, University: {Student.university}")

# s = Student('John Doe', 12345, 3.8)
# s.display_info()  # Output: Name: John Doe, ID: 12345, CGPA: 3.8, University: 
# Student.change_university("MIT")
# s.display_info()  # Output: Name: John Doe, ID: 12345, CGPA: 3.8, University: MIT
# s2 = Student('Alice', 1001, 3.9)
# s2.display_info()  # Output: Name: Alice, ID: 1001, CGPA: 3.9, University: MIT

# class Flyer:
#     def fly(self):
#         return "I believe I can fly!"

# # Single inheritance
# class Swimmer:
#     def swim(self):
#         return "I believe can swim!"
    
# # Single Inheritance
# class Crow(Flyer):
#     def caw(self):
#         return "Caw! Caw!"
    
# class Penguin(Swimmer):
#     def waddle(self):
#         return "Waddle! Waddle!"

# Multiple inheritancegit
# class Duck(Flyer, Swimmer):
#     def quack(self):
#         return "Quack! Quack!"

# # c = Crow()
# # print(c.caw())  # Output: Caw! Caw!
# # print(c.fly())  # Output: I believe I can fly!
# d = Duck()
# print(d.quack())  # Output: Quack! Quack!
# print(d.fly()) # Output: I believe I can fly!
# print(d.swim()) # Output: I believe can swim!

