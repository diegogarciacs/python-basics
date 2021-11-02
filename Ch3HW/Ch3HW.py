####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Ch 3 HW
# Due Date: 2/28/2021
# ####################################################

# 7. Color Mixer
# red, blue, and yellow are primary
# red and blue = purple
# red and yellow = orange
# blue and yellow = green
# prompt user to enter names of two primary colors
# anything but "red", "blue", or "yellow" displays error
# program should display secondary color result
red = "red"
blue = "blue"
yellow = "yellow"
color1 = input("Please tell me the 1st primary color you'd like to mix. ")
color2 = input("Please tell me the 2nd primary color you'd like to mix. ")

if (color1 != red and color1 != blue and color1 != yellow) or \
        (color2 != red and color2 != blue and color2 != yellow):
    print("Please input valid primary colors.")
elif color1 == color2:
    print("You have to mix different colors, bro.")
elif (color1 == red and color2 == blue) or (color1 == blue and color2 == red):
    print("Congratulations! You made purple.")
elif (color1 == red and color2 == yellow) or (color1 == yellow and color2 == red):
    print("Congratulations! You made orange.")
elif (color1 == blue and color2 == yellow) or (color1 == yellow and color2 == blue):
    print("Congratulations! You made green.")

# 9. Roulette Wheel Colors
# pockets are 0-36
# pocket 0 is green
# 1 - 10 odd numbers are red and even numbered are black
# 11 - 18 odd numbers are black and even are red
# 19 - 28 odd numbers are red and even are black
# 29 - 36 odd numbers are black and evens are red
# program asks user for pocket number and displays whether the pocket is green, red, or black.
print()
num = int(input("PLease give me a pocket number between 0 - 36 that you're curious about. "))
if num < 0 or num > 36:
    print("Gimme a valid number, bro.")
elif num == 0:
    print("That's green. Big money!")
elif 1 <= num <= 10:
    num = num % 2
    if (num == 0):
        print("That's black.")
    if (num != 0):
        print("That's red.")
elif 11 <= num <= 18:
    num = num % 2
    if (num == 0):
        print("That's red.")
    if (num != 0):
        print("That's black.")
elif 19 <= num <= 28:
    num = num % 2
    if (num == 0):
        print("That's black.")
    if (num != 0):
        print("That's red.")
elif 29 <= num <= 36:
    num = num % 2
    if (num == 0):
        print("That's red.")
    if (num != 0):
        print("That's black.")

# 12. Software Sales
# Sells unit for $99
# Quantity discounts are given
# 10 - 19 = 10%
# 20 - 49 = 20%
# 50 - 99 = 30%
# 100 or more 40%
# User inputs amount purchased
# Program displays amount of discount (if any) and total amount of purchase after discount
print()
num = int(input("Please tell us how many units you'd like. "))
price = 99.00
discount = 0.0
total = 0
if (num < 1):
    print("Do you even want something?")
elif 1 <= num <= 9:
     print("You want",num,"units and received a 0% discount.")
     total = num * price
     print(f"Your total is ${total:.2f}")
elif 10 <= num <= 19:
    discount = .1
    total = num * price
    final_price = total - (total * discount)
    print("You want",num,"units and received a 10% discount.")

    print(f"Your total is ${final_price:.2f}")
elif 20 <= num <= 49:
    discount = .2
    total = num * price
    final_price = total - (total * discount)
    print("You want",num,"units and received a 20% discount.")
    print(f"Your total is ${final_price:.2f}")
elif 50 <= num <= 99:
    discount = .3
    total = num * price
    final_price = total - (total * discount)
    print("You want",num,"units and received a 30% discount.")
    print(f"Your total is ${final_price:.2f}")
elif num >= 100:
    discount = .4
    total = num * price
    final_price = total - (total * discount)
    print("You want",num,"units and received a 40% discount.")
    print(f"Your total is ${final_price:.2f}")
