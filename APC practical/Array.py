# ARRAY - 10 Examples

from array import array

# Example 1: Create an array
a = array('i', [10, 20, 30, 40, 50])
print("Example 1:", a)


# Example 2: Access an element
a = array('i', [10, 20, 30, 40, 50])
print("Example 2:", a[0])


# Example 3: Access the last element
a = array('i', [10, 20, 30, 40, 50])
print("Example 3:", a[-1])


# Example 4: Add an element
a = array('i', [10, 20, 30])
a.append(40)
print("Example 4:", a)


# Example 5: Insert an element
a = array('i', [10, 20, 30])
a.insert(1, 15)
print("Example 5:", a)


# Example 6: Remove an element
a = array('i', [10, 20, 30, 40])
a.remove(20)
print("Example 6:", a)


# Example 7: Remove the last element
a = array('i', [10, 20, 30, 40])
a.pop()
print("Example 7:", a)


# Example 8: Find the length
a = array('i', [10, 20, 30, 40, 50])
print("Example 8:", len(a))


# Example 9: Find the index of an element
a = array('i', [10, 20, 30, 40, 50])
print("Example 9:", a.index(30))


# Example 10: Reverse an array
a = array('i', [10, 20, 30, 40, 50])
a.reverse()
print("Example 10:", a)