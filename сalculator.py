def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def is_even(num):
    return num % 2 == 0

def factorial(n):
    if n < 0:
        raise ValueError("Negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
