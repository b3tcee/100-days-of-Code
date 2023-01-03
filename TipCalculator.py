print("Welcome tot the Tip Calculator")

total_bill = float(input("What was the Total Bill? $"))
tip = int(input("What percentage of tip would you like to give ? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))

amount_of_tip = (tip/100) * total_bill
new_total_bill = amount_of_tip + total_bill
split_bill = new_total_bill / num_of_people
rounded_bill = round(split_bill, 2)

print (f"Each person should pay: ${rounded_bill}")
#print(rounded_bill)