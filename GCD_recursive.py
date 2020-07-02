# taking inputs a and b
a, b = map(int, input().split())


# using recursion to find GCD
def GCD(a, b):
    # base case
    if b == 0:
        return a
    else:
        k = a % b
        return GCD(b, k)


# swapping a and b if a < b
if a < b:
    temp = a
    a = b
    b = temp

print("GCD of", a, "and", b, "is", GCD(a, b))
