####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Project 2
# Due Date: 5/9/21
# ####################################################

def main():
    print("*** *** *** *** Binary Burgers Order Program *** *** *** ***")
    numorders = int(input("How many orders will there be? "))
    while numorders <= 0:
        numorders = int(input("Input was invalid. How many orders (1 or more)? "))
    for i in range(numorders):
        sand, side, drink, size, ordernum = orderTaker(i + 1)
        getPrices(sand, side, drink, size, ordernum)


def orderTaker(ordernum):
    print("*** *** *** *** Processing Order  #", ordernum, "*** *** *** ***", sep='')
    sand = int(
        input("Enter 1 for a hamburger, 2 for a cheeseburger, 3 for a chicken sandwich, or 4 for no sandwich: "))
    while sand > 4 or sand < 1:
        print("Invalid input.")
        sand = int(
            input(
                "Enter 1 for a hamburger, 2 for a cheeseburger, 3 for a chicken sandwich, or 4 for no sandwich: "))
    side = int(input("Enter 1 for french fries, 2 for onion rings, 3 for a side salad, or 4 for no side: "))
    while side > 4 or side < 1:
        print("Invalid input.")
        side = int(input("Enter 1 for french fries, 2 for onion rings, 3 for a side salad, or 4 for no side: "))
    drink = int(input("Enter 1 for Coke, 2 for Sprite, 3 for a lemonade, or 4 for a cup of water: "))
    while drink > 4 or drink < 1:
        print("Invalid Input.")
        drink = int(input("Enter 1 for Coke, 2 for Sprite, 3 for a lemonade, or 4 for a cup of water: "))
    if drink == 4:
        size = -1
    if 0 < drink < 4:
        size = int(input("Enter 1 for Small, 2 for Medium, 3 for a Large: "))
        while size < 1 or size > 3:
            print("Invalid input.")
            size = int(input("Enter 1 for Small, 2 for Medium, 3 for a Large: "))
    return sand, side, drink, size, ordernum


def getPrices(sand, side, drink, size, ordernum):
    # save sand prices and strings
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
    elif sand == 4:
        wich = "None"
        sandPrice = 0.00
    # save side prices and strings
    if 0 > side > 3:
        sidePrice = 0.00
    elif side == 1:
        sidePrice = 2.25
        sideName = "French fries"
    elif side == 2:
        sidePrice = 1.75
        sideName = "Onion Rings"
    elif side == 3:
        sidePrice = 1.50
        sideName = "Side Salad"
    elif side == 4:
        sideName = 'None'
        sidePrice = 0.00
    # save drink name
    if drink == 4:
        drinkPrice = 0.00
        drinkName = "Cup of Water"
    elif drink == 1:
        drinkName = "Coke"
    elif drink == 2:
        drinkName = "Sprite"
    elif drink == 3:
        drinkName = "Lemonade"
    # save sizes and prices
    if size == 1:
        drinkSize = "Small"
        drinkPrice = 1.50
    if size == 2:
        drinkSize = "Medium"
        drinkPrice = 2.25
    if size == 3:
        drinkSize = "Large"
        drinkPrice = 2.75
    if size == -1:
        drinkPrice = 0.00
        drinkSize = ''
    drinkName = drinkSize + " " + drinkName
    if drink == 4:
        drinkName = "Cup of Water"
    calculateReceipt(ordernum, wich, sandPrice, sideName, sidePrice, drinkName, drinkPrice)


def calculateReceipt(ordernum, wich, sandPrice, side, sidePrice, drinkName, drinkPrice):
    if ordernum == 1:
        file = open("Reciept.txt", 'w')
    else:
        file = open("Reciept.txt", 'a')
    sub = "Subtotal"
    tax = "Sales Tax"
    tot = "Total"
    subtotal = drinkPrice + sidePrice + sandPrice + 0.00
    totalTax = .08 * subtotal
    # beverage = drinkSize + " " + drinkName
    total = totalTax + subtotal
    file.write("~~~~~~~~********Total for Order #")
    file.write(str(ordernum))
    file.write("********~~~~~~~~\n\n")
    if wich != "None":
        receipt = f"{wich:<25}" f"${sandPrice:<.2f}\n"
        file.write(receipt)
    if side != "None":
        receipt = f"{side:<25}" f"${sidePrice:<.2f}\n"
        file.write(receipt)
    # if 0 < drink < 4:
    receipt = f"{drinkName:<25}"  f"${drinkPrice:<.2f}\n"
    file.write(receipt)

    file.write("------------------------------\n")
    receipt = (f"{sub:<25}" + f"${subtotal:<.2f}\n")
    file.write(receipt)
    receipt = (f"{tax:<25}" + f"${totalTax:<.2f}\n")
    file.write(receipt)
    receipt = (f"{tot:<25}" + f"${total:<.2f}\n\n")
    file.write(receipt)
    file.close()
main()