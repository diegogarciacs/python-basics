####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Chapter 5 Homework
# Due Date: 3/28/2020
# ####################################################
import random

def main():
    print("Here's a list of prime numbers.")
    prime_list() # 18 function call to print prime numbers 0 - 100
    print()
    prime = int(input("Enter a number to check if it's prime. ")) # input to see if prime
    result = is_prime(prime) # function call
    if result: # if true, print prime
        print("It's prime!")
    else:
        print("It's not!")
    print()
    loanAmount = float(input("How much money will you be investing? "))
    interest = float(input("What kind of interest rate are you looking for (percentage)? "))
    months = int(input("How many months do you want? "))
    loan_payments(loanAmount, interest, months)
    rockPaperScissors()
# 17
def is_prime(num):
    if (num <= 1): # must be integer larger than 1
        return False

    for i in range(2,num): # checks numbers from 2 to num - 1
        if num % i == 0: # if the number can be evenly divided by anything besides itself, it is not prime
            return False # the moment it is, we return fasle

    return True
# 18
def prime_list():
    count = 0
    for i in range(0,101): # iterate from 0 - 100
        if is_prime(i): # send each i to is_prime() function
            print(i, end=" ")
            count = count + 1 # count every return
    print()

    print(f"Total of {count} prime numbers between 0 and 100.")

# 19

def loan_payments(amount, rate, months):
    rate = rate / 100 # change from % to rate
    future_value = (amount) * (1+rate)**months # calc future investment
    print(f"Your future value of the account will be ${future_value:,.2f}") # print investment result

def rockPaperScissors():
    print("Let's play a game, shall we?")
    print()
    valid = True
    again = "Y"
    while again == 'y' or again == 'Y':
        again = input("You wanna play? (y/n) ")
        if again == 'y' or again == 'Y':
            print("Choose 1 for rock, 2 for paper, and 3 for scissors. Anything else and you lose.")
            choice = int(input("Give me your best shot. "))
            if choice == 1:
                print("Rock!")
            elif choice == 2:
                print("Paper!")
            elif choice == 3:
                print("Scissors!")
            else:
                print("You didn't make a valid choice! You lose!")
                valid = False
            computer = random.randrange(1, 4)
            if computer == 1 and valid == True:
                print("Computer chooses: Rock!")
            elif computer == 2 and valid == True:
                print("Computer chooses: Paper!")
            elif computer == 3 and valid == True:
                print("Computer chooses: Scissors!")

            if choice == computer:
                print("Tie!")
            elif choice == 1 and computer == 2:
                print("Paper beats rock, computer wins!")
            elif choice == 1 and computer == 3:
                print("Rock beats scissors, player wins!")
            elif choice == 2 and computer == 1:
                print("Paper beats rock, player wins!")
            elif choice == 2 and computer == 3:
                print("Scissors beats paper, computer wins!")
            elif choice == 3 and computer == 1:
                print("Rock beats scissors, computer wins!")
            elif choice == 3 and computer == 2:
                print("Scissors beats paper, player wins!")
        else:
            print("See ya!")







main()