####################################################
# CS 31, Prof. Muldrow
# Name: Diego Garcia
# Assignment: Ch 9 HW
# Due Date: 5/17/21
# ####################################################

def main():
    moonMR = {'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244}
    moonSG = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    moonOP = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}
    print("Rooms: CS101, CS102, CS103, NT110, CM241.")
    key = input("What room would you like to learn about? ")
    if key in moonMR:
        print(key,"is:",moonMR[key])
        print(key,"is:",moonSG[key])
        print(key,"is:",moonOP[key])
    else:
        print("That is not a Galilean moon of Jupiter.")

    file = open("words1.txt",'r')
    words = []
    for line in file:
        for word in line.split():
            words.append(word)
    set1 = set(words)
    print(set1)
    file2 = open("words2.txt",'r')
    words2 = []
    for line in file2:
        for word in line.split():
            words2.append(word)
    set2 = set(words2)
    print()
    print("Set 1 unique words:",set1)
    print("Set 2 unique words:",set2)
    print()
    print("List of all words in words1.txt",words)
    print("List of all words in words2.txt",words2)
    print()
    print("List of the words that appear in the first file but not the second:",set1 - set2)
    print()
    print("List of the words that appear in the second file but not the first:",set2 - set1)
    print()
    print("List of the words that appear in either the first or second file, but not both:",)
    print()
    print("list of the words that appear in either the first or second file, but not both:",set1 ^ set2)



    file.close()

main()

