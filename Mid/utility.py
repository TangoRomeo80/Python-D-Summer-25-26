# Example utility file

PI = 3.14159

def add(a, b):
    return a + b

class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b