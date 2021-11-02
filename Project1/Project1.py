####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Project 1
# Due Date: 3/22/21
# ####################################################
# initialize prices
sandPrice = 0.00
sidePrice = 0.00
drinkPrice = 0.0
salesTax = 0.08
# initialize strings
wich = ""
drinkSize = ""
drinkName = ""
sideName = ""
print()
print("*** *** *** *** Binary Burgers Order Program *** *** *** ***")
print()
# take input
sand = int(input("Enter 1 for a hamburger, 2 for a cheeseburger, 3 for a chicken sandwich, or 4 for no sandwich: "))
# save price and name of input
if 0 > sand > 3:
    sandPrice = 0.00
elif sand == 1:
    sandPrice = 2.75
    wich = "Hamburger"
elif sand == 2:
    sandPrice = 3.25
    wich = "Cheeseburger"
elif sand == 3:
    sandPrice = 2.50
    wich = "Chicken Sandwich"
# input
side = int(input("Enter 1 for french fries, 2 for onion rings, 3 for a side salad, or 4 for no side: "))
# save price and name of input
if 0 > side > 3: 
    sidePrice = 0.00
elif side == 1:
    sidePrice = 2.25
    sideName = "French side"
elif side == 2:
    sidePrice = 1.75
    sideName = "Onion Rings"
elif side == 3:
    sidePrice = 1.50
    sideName = "Side Salad"
# input
drink = int(input("Enter 1 for Coke, 2 for Sprite, 3 for a lemonade, or 4 for a cup of water: "))
# save price and name of input
if 0 > drink or drink > 3:
    drinkPrice = 0.00
    drinkName = "Water"
    drinkSize = "Medium"
elif drink == 1:
    drinkName = "Coke"
elif drink == 2:
    drinkName = "Sprite"
elif drink == 3:
    drinkName = "Lemonade"
# if input is flavoured, take size input
if 0 < drink < 4:
    size = int(input("Enter 1 for Small, 2 for Medium, 3 for a Large: "))
    # save price and name of input
    if size == 1:
        drinkSize = "Small"
        drinkPrice = 1.50
    if size == 2:
        drinkSize = "Medium"
        drinkPrice = 2.25
    if size == 3:
        drinkSize = "Large"
        drinkPrice = 2.75

print()

sub = "Subtotal"
tax = "Sales Tax"
tot = "Total"
subtotal = drinkPrice + sidePrice + sandPrice + 0.00
totalTax = salesTax * subtotal
beverage = drinkSize + " " + drinkName
total = totalTax + subtotal
print("Here is your order:")
if 0 < sand < 4:
    print(f"{wich:<25}" + f"${sandPrice:<.2f}")

if 0 < side < 4:
    print(f"{sideName:<25}" + f"${sidePrice:<.2f}")
# if 0 < drink < 4:
print(f"{beverage:<25}" + f"${drinkPrice:<.2f}")

print("------------------------------")
print(f"{sub:<25}" + f"${subtotal:<.2f}")
print(f"{tax:<25}" + f"${totalTax:<.2f}")
print(f"{tot:<25}" + f"${total:<.2f}")

