a = 10
b = 20

print("a =", a)
print("b =", b)
print()

print("1. Equal to (a == b):", a == b)
print("2. Not equal to (a != b):", a != b)
print("3. Greater than (a > b):", a > b)
print("4. Less than (a < b):", a < b)
print("5. Greater than or equal to (a >= b):", a >= b)
print("6. Less than or equal to (a <= b):", a <= b)

print("\n--- String Comparison ---")

x = "apple"
y = "banana"

print("x =", x)
print("y =", y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)

print("\n--- Chained Comparison ---")

n = 15
print("n =", n)
print("10 < n < 20:", 10 < n < 20)
print("n > 10 and n < 20:", n > 10 and n < 20)

print("\n--- Object Identity vs Equality ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

a,b = 10,20