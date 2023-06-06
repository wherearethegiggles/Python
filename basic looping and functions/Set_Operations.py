fruits = {'apple', 'banana', 'orange'}

# Adding an element to the set
fruits.add('grape')
print(fruits)  # Output: {'banana', 'orange', 'apple', 'grape'}

# Removing an element from the set using discard()
fruits.discard('banana')
print(fruits)  # Output: {'orange', 'apple', 'grape'}

# Removing an element from the set using remove()
fruits.remove('orange')
print(fruits)  # Output: {'apple', 'grape'}

# Removing and returning an arbitrary element using pop()
popped_element = fruits.pop()
print("Popped Element:", popped_element)
print(fruits)  # Output: {'grape'}

# Clearing the set
fruits.clear()
print(fruits)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Union of sets
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {4, 5}

# Difference of sets
difference_set = set1.difference(set2)
print("Difference:", difference_set)  # Output: {1, 2, 3}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7}