#  # ICA2, Part 1
game1 = int(input("Enter game 1 score: "))
game2 = int(input("Enter game 2 score: "))
game3 = int(input("Enter game 3 score: "))

# age = int(input("How old are you? "))
avg = (game1+game2+game3) / 3
print(f'Your average is {avg:.1f}')
print()

if avg >= 100:
    print("Bowling average meets requirement.")
    print()
    if avg < 120:
        print("Join beginner league.")
    elif avg < 150:
        print("Join intermediate league.")
    else:
        print("Join advanced league.")
else:
    print("Keep training, kid.")

 # ICA2, Part 3 & 4

num = int(input("Please enter a number: "))
bad = num < 1 or num > 7
if bad:
    print("Invalid number.")
elif num == 1:
    print("Monday.")
elif num == 2:
    print("Tuesday.")
elif num == 3:
    print("Wednesday.")
elif num == 4:
    print("Thursday.")
elif num == 5:
    print("Friday.")
elif num == 6:
    print("Saturday.")
elif num == 7:
    print("Sunday.")


