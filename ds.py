# Creating tuple
person = ("Aditya", 28, "Engineer")

# Accessing elements
print("Name:", person[0])
print("Age:", person[1])
print("Profession:", person[2])

# Looping 
for item in person:
    print(item)

# Tuple unpacking
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}.")

from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # deque

#list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
for fruit in fruits:
    print(fruit)

#sets

# Creating sets
fruits = {"apple", "banana", "cherry"}
print("Initial set:", fruits)

# Adding an item
fruits.add("orange")
print("After adding 'orange':", fruits)

# Updating set with multiple items
fruits.update(["mango", "grape"])
print("After updating with ['mango', 'grape']:", fruits)

# Removing an item (raises KeyError if not present)
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Discarding an item (no error if not present)
fruits.discard("pear")  # pear is not in the set
print("After discarding 'pear':", fruits)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nSet1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)             # {1, 2, 3, 4, 5}
print("Intersection:", set1 & set2)      # {3}
print("Difference (set1 - set2):", set1 - set2)  # {1, 2}
print("Symmetric difference:", set1 ^ set2)     # {1, 2, 4, 5}

# Checking membership
print("Is 2 in set1?", 2 in set1)

# Set length
print("Length of fruits set:", len(fruits))

# Clearing a set
fruits.clear()
print("After clearing fruits:", fruits)

