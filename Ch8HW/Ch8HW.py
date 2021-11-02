####################################################
# CS 31, Prof. Muldrow
# Name: Diego Garcia
# Assignment: Ch 8 HW
# Due Date: 5/9/21
####################################################

# 3. takes string from user mm/dd/yyyy and prints date in format March 12, 2018

def main():
    date = input("Please input a date in the form: mm/dd/yyyy: ")
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']

    if len(date) != 10:
        date = input("Date is inputted incorrectly. mm/dd/yyyy: ")

    mon = date[:2]
    if int(mon) > 12 or int(mon) < 1:
        date = input("Month needs to be between 1-12. mm/dd/yyyy: ")
        mon = date[:2]
    day = date[3:5]
    year = date[6:len(date)]
    # mon = mon.lstrip('0')
    mon = month[int(mon) - 1]

    print(mon, " ", day, ", ", year, sep='')
    code = input("Please input what you'd like to convert to morse code. ")
    morseCode(code)
    num = input("Please input a number you'd like to decipher. Ex. 555-GET-FOOD: ")
    tele(num)

# 4. Morse Code Converter
def morseCode(txt):
    morse = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....',
             '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
             '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
             '-.-', '--..']
    english = [' ', ',','.','?','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J'
               ,'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    code = ''
    txt = txt.upper()

    for ch in txt:
        index = english.index(ch)
        code = code + morse[index]
    print(code)

    # other version
    # for obj in english:
    #     index = english.index(obj)
    #     for ch in txt:
    #         if obj == ch:
    #             code = code + morse[index]
    # print(code)

# 5. Alphabetic Telephone Number Translator

def tele(num):
    number = ''
    num = num.upper()
    for x in num:
        if x == 'A' or x == 'B' or x == 'C':
            number = number + '2'
        elif x == 'D' or x == 'E' or x == 'F':
            number = number + '3'
        elif x == 'G' or x == 'H' or x == 'I':
            number = number + '4'
        elif x == 'J' or x == 'K' or x == 'L':
            number = number + '5'
        elif x == 'M' or x == 'N' or x == 'O':
            number = number + '6'
        elif x == 'P' or x == 'Q' or x == 'R' or x == 'S':
            number = number + '7'
        elif x == 'T' or x == 'U' or x == 'V':
            number = number + '8'
        elif x == 'W' or x == 'X' or x == 'Y' or x == 'Z':
            number = number + '9'
        else:
            number = number + x
    print(number)

main()
