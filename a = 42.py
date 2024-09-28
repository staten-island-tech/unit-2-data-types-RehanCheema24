a = 42
b = 54
for i in range(2, a + 1):
    if a % i == 0 and b % i == 0:
        gcf = i

print("The GCF of these 2 numbers is", gcf)

