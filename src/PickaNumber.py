import random
NumPool = random.randint(1, 10)
Player = input("Pick a Number Between 1 and 1\n")
if int(Player) == NumPool:
    print("Correct!")
else:
    print("Incorrect, Try Again!")
print(NumPool)