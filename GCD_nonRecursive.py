# taking inputs a and b
a, b = map(int, input().split())

# swapping a and b if a < b
if a < b:
    temp = a
    a = b
    b = temp

num1 = a
num2 = b

# iterating until b = 0
while b != 0:
    k = a % b
    a = b
    b = k

print("GCD of", num1, "and", num2, "is", a)
