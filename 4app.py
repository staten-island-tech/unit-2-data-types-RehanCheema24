"""  x = "this is a thing"
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
pri("Even") """
""" def calculate_tip(bill, service):
    if service == "bad":
        tip_percentage = 0
    elif service == "okay":
        tip_percentage = 15
    elif service == "good":
        tip_percentage = 20
    elif service == "great":
        tip_percentage = 25
    else:
        return "Invalid service rating"
    
    tip_amount = (tip_percentage / 100) * bill
    return tip_amount """

""" def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
number = 42
factors_of_number = find_factors(number)
print(f"The factors of {number} are: {factors_of_number}") """
""" a = 42
b = 54
for i in range(2, a + 1):
    if a % i == 0 and b % i == 0:
        gcf = i
print("The GCF of these 2 numbers is", gcf) """


