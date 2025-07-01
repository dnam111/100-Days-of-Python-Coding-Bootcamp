print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
decimal_tip = float(tip/100)
sum_tip= decimal_tip*bill
sum_bill=sum_tip+bill
bill_per_person=sum_bill/people
twodecimal=round(bill_per_person,2)
print(f"Each person should pay {twodecimal}")


