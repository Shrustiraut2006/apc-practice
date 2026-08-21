# LAMBDA FUNCTION - 10 Examples

# Example 1: Square
square = lambda x: x * x
print("Example 1:", square(5))


# Example 2: Addition
add = lambda a, b: a + b
print("Example 2:", add(10, 20))


# Example 3: Subtraction
subtract = lambda a, b: a - b
print("Example 3:", subtract(20, 5))


# Example 4: Multiplication
multiply = lambda a, b: a * b
print("Example 4:", multiply(4, 5))


# Example 5: Division
divide = lambda a, b: a / b
print("Example 5:", divide(20, 5))


# Example 6: Cube
cube = lambda x: x ** 3
print("Example 6:", cube(3))


# Example 7: Check even number
even = lambda x: x % 2 == 0
print("Example 7:", even(10))


# Example 8: Find maximum
maximum = lambda a, b: max(a, b)
print("Example 8:", maximum(10, 20))


# Example 9: Find minimum
minimum = lambda a, b: min(a, b)
print("Example 9:", minimum(10, 20))


# Example 10: Convert names to uppercase
names = ["ram", "amit", "priya"]

result = list(map(lambda x: x.upper(), names))

print("Example 10:", result)