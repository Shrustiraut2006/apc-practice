# FUNCTION - 10 Examples


# Example 1: Simple function
def greet():
    print("Hello")

greet()


# Example 2: Function with one argument
def greet_name(name):
    print("Hello", name)

greet_name("Shrusti")


# Example 3: Function with two arguments
def add(a, b):
    print(a + b)

add(10, 20)


# Example 4: Function with return value
def square(n):
    return n * n

print(square(5))


# Example 5: Function to check even number
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(even(10))


# Example 6: Function to multiply two numbers
def multiply(a, b):
    return a * b

print(multiply(4, 5))


# Example 7: Function to calculate area
def area(length, width):
    return length * width

print(area(5, 4))


# Example 8: Function to find maximum
def maximum(a, b):
    return max(a, b)

print(maximum(10, 20))


# Example 9: Function with default argument
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Shrusti")


# Example 10: Factorial using function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(factorial(5))