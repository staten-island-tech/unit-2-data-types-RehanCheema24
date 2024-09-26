""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" input("How are you")
input("good") """
""" day_of_week = input("Tuesday")
if day_of_week == "Tuesday":
    print("correct")
else:
    print("incorrect")
day_of_week = Tuesday
 """
 
""" temp = 58
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
""" values = [2,4,6,8,10]
x = values
if x == values:
    print ("Even")
else:
    print ("Odd") """
""" x= 31
quotient, remainder = divmod(x,2)
if remainder == 1:
    print ("Odd")
else:
    print("Even") """
""" def bad(q):
    q = ("0%")
service = bad
if service == bad:
    print("0%")
def okay(m):
    m = ("15%")
service = okay
if service == okay:
    print ("15%")
def good(v):
    q = ("20%")
service = good
if service == good:
    print("20%")
def great(s):
    s = ("25%")
service = great
if service == great:
    print("25")  """
""" def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
num = 112
print("Factors of", num, "are:", find_factors(num)) """
""" import math
num1 = int(input("Input num 1: "))
num2 = int(input("Input num 2: "))
gcf = math.gcd(num1, num2)
print("The GCF of these 2 numbers is", gcf) """
celebrity = input("print celebrity:")
verb = input("Print a verb:")
noun = input("Print a noun:")
num = input("Print a number:")
future_tense_verb = input("Print a future tense verb:")
madlib = f"Last weekend, {celebrity} decided to {verb} at the park. \
They brought a {noun} and played for {num} hours straight. \
Afterwards, they said they {future_tense_verb} again next weekend."
print(madlib)
 