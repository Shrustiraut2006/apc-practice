# FROZEN SET - 10 Examples


# Example 1: Create a frozenset
s = frozenset([1, 2, 3, 4, 5])
print("Example 1:", s)


# Example 2: Duplicate values are removed
s = frozenset([1, 2, 2, 3, 3, 4])
print("Example 2:", s)


# Example 3: Check whether an element exists
s = frozenset([1, 2, 3])
print("Example 3:", 2 in s)


# Example 4: Find the length
s = frozenset([10, 20, 30, 40])
print("Example 4:", len(s))


# Example 5: Union
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print("Example 5:", a.union(b))


# Example 6: Intersection
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print("Example 6:", a.intersection(b))


# Example 7: Difference
a = frozenset([1, 2, 3])
b = frozenset([2, 3])
print("Example 7:", a.difference(b))


# Example 8: Symmetric difference
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print("Example 8:", a.symmetric_difference(b))


# Example 9: Loop through a frozenset
s = frozenset(["A", "B", "C"])

print("Example 9:")
for item in s:
    print(item)


# Example 10: Use frozenset as a dictionary key
s = frozenset([1, 2, 3])
student = {s: "Numbers"}

print("Example 10:", student)