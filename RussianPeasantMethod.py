# taking inputs a and b
a, b = map(int, input().split())

# list to contain the numbers which should be summed
nums = []
num1 = a
num2 = b

# swap if a > b
if a > b:
    temp = a
    a = b
    b = temp

# using Russian Peasant method
while a != 1:
    if a % 2 == 1:
        nums.append(b)
    a = int(a / 2)
    b = b + b

nums.append(b)

print(num1, "x", num2, "=", sum(nums))
