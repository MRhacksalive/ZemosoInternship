x = 5 + 2
print(x)

name = "Alice"
a, b, c = 1, 2, 3

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

for i in range(3):
    print("For loop:", i)

count = 0
while count < 3:
    print("While loop:", count)
    count += 1

def greet(name):
    print("Hello", name)

greet("Bob")

import math
print("Square root of 16 is", math.sqrt(16))

def placeholder():
    pass

for i in range(5):
    if i == 3:
        break
    print("Break example:", i)

for i in range(5):
    if i == 3:
        continue
    print("Continue example:", i)

def add(a, b):
    return a + b

result = add(3, 4)
print("Return example:", result)

for i in range(2, 100, 2): #start,stop,step
    print(i)

