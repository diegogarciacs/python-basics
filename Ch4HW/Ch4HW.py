####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Ch 4 Homework
# Due Date: 03/08/2021
# ####################################################
# 12. Calculating the Factorial of a number
# Non-negative integer
factorial = int(input("Enter the factorial bro. "))

while factorial < 0:
    factorial = int(input("Enter a positive number please. "))
total = 1
for x in range(1,factorial+1):

    total = total * x
print("The factorial of",factorial,"is",total)

# 13. Population
# User enters "Starting number of organisms: 2"
# User enters "Average daily increase: 30%"
# User enters "Number of days to multiply: 10"
pop = int(input("Gimme starting number of organisms: "))
inc = int(input("Average daily increase: "))
days = int(input("Number of days to multiply: "))
inc = inc / 100
for x in range(1,days+1):
    print(f"{x}\t\t{pop:<16.6f}")
    pop = (inc * pop) + pop
# 15. Draw Pattern
for x in range(6):
    print("#",end='')
    for y in range(x):
        print(" ",end="")
    print("#")