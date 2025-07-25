# Index: 0 1 2 3 4
# Array: [5, 10, 20, 25]

#Updating an array

# Array in Python is called List
arr = [10, 20, 30, 40, 50]

# Access
# print(arr[2])

# Update
arr[2] = 55

# print(arr[2])

#Insert at the end
arr.append(60)

# print(arr)

# Insert at a position
arr.insert(2, 25)

# print(arr)

# Delete an Element

arr.pop(3)

# print(arr)

# Search for a value
if 10 in arr:
    print("found 10")