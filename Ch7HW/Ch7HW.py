####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Chapter 7 HW
# Due Date: 5/2/2021
# ####################################################

# 11 Lo Shu Magic Square
# contains the numbers 1 - 9 exactly, the sum of each row, each column, and each diagonal add up to the same number
# function that accepts two dimensional list as argument and determines if it is a Lo Shu Magic Square
# 11
import random
import matplotlib.pyplot as plt
def main():
    list = [[4,9,2],
            [3,5,7],
            [8,1,6]]
    magic = loShu(list)
    if magic:
        print("It's magic!")
    else:
        print("It's not")
    magicBall()
    weeklyGas()
def loShu(list):
    row1 = 0
    row2 = 0
    row3 = 0
    column1 = 0
    column2 = 0
    column3 = 0
    magic = False
    for x in range(1):
        for i in range(3):
            row1 = row1 + list[x][i]
            row2 = row2 + list[x+1][i]
            row3 = row3 + list[x+2][i]

    for x in range(3):
        for i in range(1):
            column1 = column1 + list[x][i]
            column2 = column2 + list[x][i+1]
            column3 = column3 + list[x][i+2]
    diagonal1 = list[0][0] + list[1][1] + list[2][2]
    diagonal2 = list[0][2] + list[1][1] + list[2][0]
    if row1 == row2 == row3 == column1 == column2 == diagonal1 == diagonal2:
        magic = True
        return magic
# 13 Program that simulates magic 8 ball
# Read responses from external txt, store in list separately
# ask user a question, then display random response. Repeat until user is ready to quit
def magicBall():
    file = open('8_ball_responses.txt', 'r')
    responses = []
    responses = file.readlines() # read contents into list
    index = 0
    while index < len(responses):
        responses[index] = responses[index].rstrip('\n')
        index += 1
    file.close()
    print("Hello my child, welcome to my emporium.")
    play = 'y'
    while play == 'y' or play == 'Y':

        question = input("What would you like to ask the magical 8 ball? ")
        print()
        print(responses[random.randint(0,12)])
        print()
        play = input("Would you like to ask another question? (y/n) ")
        print()
# 15 1994 Weekly Gas
def weeklyGas():
    file = open("1994_Weekly_Gas_Averages.txt",'r')
    gas = []
    weeks = []
    actualWeeks = []
    gas = file.readlines()
    index = 0
    while index < len(gas):
        gas[index] = float(gas[index].rstrip('\n'))
        index += 1
    file.close()
    for x in range(13):
        weeks.append((x+1) * 4)
    for x in range(52):
        actualWeeks.append(x+1)

    plt.figure()
    x_cor = actualWeeks
    y_cor = gas
    plt.plot(x_cor,y_cor)
    plt.title("1994 Weekly Gas Averages Per Week")
    plt.xlabel("Week")
    plt.ylabel("Gas price per gallon")
    plt.xticks(weeks,weeks)
    plt.yticks([0.95,1.00,1.05,1.10,1.15,1.20],['$0.95','$1.00','$1.05','$1.10','$1.15','$1.20'])
    plt.ylim([0.95, 1.20])
    plt.grid(True)
    plt.show()
main()