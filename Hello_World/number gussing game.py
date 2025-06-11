import random

i = random.randrange(0, 100)
count = 0

while True:
    number = int(input("Enter a value: "))

    if number == i:
        print("Your number", i , "is correct")
        count += 1
        break
    elif number > i:
        print("Your number is too big")
        count += 1
    elif number < i:
        print("Your number is too small")
        count += 1
    else:
        print("you are wrong")
print("Your moves are:", count)