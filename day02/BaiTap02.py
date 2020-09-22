import math

n = int(input("n = "))
x = float(input("x = "))
s1 = None
s2 = None

for i in range(n + 1):
    s1 = s1 + x**i
    s2 += -1**i * x**i

print("s1 = ", str(s1))
print("s2 = ", str(s2))
