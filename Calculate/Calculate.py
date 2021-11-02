# ICA 1, Part 1
amount = float(input("Enter purchase amount: "))
STATE = 0.05
COUNTY = 0.025
state_tax = amount * STATE # state sales tax
county_tax = amount * COUNTY # county sales tax
total_tax = state_tax + county_tax
total_sale = amount + total_tax
print(f"Purchase amount: ${amount:.2f}")
print(f"State Sales Tax: ${state_tax:.2f}")
print(f"County Sales Tax: ${county_tax:.2f}")
print(f"Total Sales Tax: ${total_tax:.2f}")
print(f"Total Sale: ${total_sale:,.2f}")
print()
#8
check = float(input("How much was the dinner? "))
TIP = 0.18
TAX = 0.07
tip = check * TIP
tax = check * TAX
total = check + tax + tip
print("Purchase amount: $",format(check, '.2f'),
      "\nSales Tax: $",format(tax, '.2f'),
      "\nTip: $", format(tip, '.2f'),
      "\nTotal: $", format(total, '.2f'),sep='')
