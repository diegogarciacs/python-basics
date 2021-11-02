####################################################
# CS 31, Prof. Muldrow
# Name: Diego O Garcia
# Assignment: Chapter 6 Homework
# Due Date: 04/18/2021
# ####################################################
# 6 read numbers from numbers.txt and average all numbers
# 9 Exception handing
import random
try: # try our block of code
    sum = 0 # initialize sum
    count = 0 # initialize counter
    inf = open("numbers.txt", 'r') # open file in read mode
    for num in inf: # iterate through each line of file
        num = int(num) # cast first line to int
        sum = sum + num # add to sum
        count = count + 1 # count 1 per loop
    total = float(sum / count)
    print(f"Total average is: {total:.2f}")
except IOError: # Throw exception if file does not open
    print("File did not open.")
except ValueError: # Throw exception if there is an invalid data type
    print("Could not convert data to an integer")

# 7 Program that writes a series of random numbers to file. 1 - 500. User specified number of numbers.

outfile = open("random.txt", 'w') # open file in write mode
nums = int(input("Tell me how many random numbers you'd like. ")) # ask user for number of randoms
for x in range(nums): # iterate through users number of randoms
    number = str(random.randint(1, 501)) # generate random number 1 - 500
    outfile.write(number + "\n") # write to random.txt with newline
outfile.close()  # close after loop

# 8 Random Number File Reader
# displays total of numbers in random.txt & the number of random numbers
inf = open("random.txt" ,'r') # open random.txt in read mode
total = 0
count = 0
for num in inf:
    num = int(num)
    total = num + total
    count = count + 1
print("The total is",total,"and the number of randoms in the file is",count)

# 10 Create golf.txt with save a players name and golf score
# then will read records from golf.txt
# write
outfile = open("golf.txt",'w')
players = int(input("How many player records do you need? "))
for x in range(1,players+1):
    print("Enter data for player #",x,sep='')
    name = input("Name: ")
    score = input("Score: ")
    outfile.write(name + "\n")
    outfile.write(score + "\n")
outfile.close()
# read
infile = open("golf.txt",'r')
print()
print("Names                         Scores")
for x in infile:
    name = x.rstrip("\n")
    score = infile.readline().rstrip("\n")
    print(f"{name:<30}{score:>}")
infile.close()
