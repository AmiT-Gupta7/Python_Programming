collection = set() # Create an empty set

print(type(collection)) # Output: <class 'set'>

# Add element to the set
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2) # Duplicate, will not be added
print(collection)

# Remove element from the set
collection.remove(2)
print(collection)

# Check if an element is in the set
print(3 in collection)
print(2 in collection)

# Iterate through the set
for item in collection:
    print(item)

# Clear the set
collection.clear()
print(collection)

