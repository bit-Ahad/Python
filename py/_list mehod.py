b = [1, 33, 4583, 67, 159]
print("Original list:", b)

# Append 11 to the list
b.append(11)
print("After append(11):", b)   # Do NOT print b.append(11), it returns None

# Sort in ascending order
b.sort()
print("After sort():", b)

# Sort in descending order
b.sort(reverse=True)
print("After sort(reverse=True):", b)

# Reverse the list
b.reverse()
print("After reverse():", b)

# Count occurrences of 33
count_33 = b.count(33)
print("Count of 33:", count_33)

# Copy the list and change index 3
m = b.copy()
m[3] = 0
print("Copied list m with change:", m)
print("Original list b remains:", b)

# Insert 99999999 at index 3
b.insert(3, 99999999)
print("After insert(3, 99999999):", b)

# Extend Add another list at the end of a list
a = [1,2,3]
b = [3,4,5]
a.extend(b)
print(a)
# Append create a nested list a list in another  list
a = [1,2,3]
b = [3,4,5]
a.append(b)
print(a)
# List can be contegnate like simple string
a = [1,2,3]
b = [3,4,5]
d = a + b
print("Contgnate using plus  ",d)