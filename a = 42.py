""" a = 42
b = 54
for i in range(2, a + 1):
    if a % i == 0 and b % i == 0:
        gcf = i
print("The GCF of these 2 numbers is", gcf) """
def calculate_tip(bill, service):
    tip_percentages = {"bad": 0, "okay": 15, "good": 20, "great": 25}
    
    tip_percentage = tip_percentages.get(service, None)
    
    if tip_percentage is None:
        return "Invalid service rating"
    
    tip_amount = (tip_percentage / 100) * bill
    total_amount = bill + tip_amount
    return tip_amount, total_amount


