# DICTIONARY - 10 Examples


# Example 1: Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE"
}
print("Example 1:", student)


# Example 2: Access a value using key
student = {
    "name": "Rahul",
    "age": 20
}
print("Example 2:", student["name"])


# Example 3: Add a new key-value pair
student = {
    "name": "Rahul",
    "age": 20
}
student["city"] = "Kolhapur"
print("Example 3:", student)


# Example 4: Update a value
student = {
    "name": "Rahul",
    "age": 20
}
student["age"] = 21
print("Example 4:", student)


# Example 5: Delete a key-value pair
student = {
    "name": "Rahul",
    "age": 20
}
del student["age"]
print("Example 5:", student)


# Example 6: Get all keys
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE"
}
print("Example 6:", student.keys())


# Example 7: Get all values
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE"
}
print("Example 7:", student.values())


# Example 8: Loop through a dictionary
student = {
    "name": "Rahul",
    "age": 20
}

print("Example 8:")
for key, value in student.items():
    print(key, value)


# Example 9: Check whether a key exists
student = {
    "name": "Rahul",
    "age": 20
}
print("Example 9:", "name" in student)


# Example 10: Dictionary with multiple students
students = {
    1: "Rahul",
    2: "Amit",
    3: "Priya"
}

print("Example 10:", students[2])