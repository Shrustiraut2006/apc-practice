# SET - 10 Examples


# Example 1: Create a set
s = {1, 2, 3, 4, 5}
print("Example 1:", s)


# Example 2: Duplicate values are removed
s = {1, 2, 2, 3, 3, 4}
print("Example 2:", s)


# Example 3: Add an element
s = {1, 2, 3}
s.add(4)
print("Example 3:", s)


# Example 4: Remove an element
s = {1, 2, 3, 4}
s.remove(2)
print("Example 4:", s)


# Example 5: Discard an element
s = {1, 2, 3, 4}
s.discard(3)
print("Example 5:", s)


# Example 6: Union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Example 6:", a.union(b))


# Example 7: Intersection of two sets
a = {1, 2, 3}
b = {2, 3, 4}
print("Example 7:", a.intersection(b))


# Example 8: Difference of two sets
a = {1, 2, 3}
b = {2, 3, 4}
print("Example 8:", a.difference(b))


# Example 9: Symmetric difference
a = {1, 2, 3}
b = {2, 3, 4}
print("Example 9:", a.symmetric_difference(b))


# Example 10: Check whether an element exists
s = {10, 20, 30}
print("Example 10:", 20 in s)