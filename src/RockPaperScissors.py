import random

Pool=["Rock", "Paper", "Scissors"]
Play = Pool.pop(random.randint(0, len(Pool)-1))
Player = input("Write Rock, Paper, Or Scissors\n") #PLayer chooses Rock, Paper, or Scissors
print("Bot Picks" , Play)

if Player.lower() == Play.lower():
    print("Tie")
elif Player.lower() == "rock" and Play.lower() == "paper":
    print("Player Loses")
elif Player.lower() == "rock" and Play.lower() == "scissors":
    print("Player Wins")
elif Player.lower() == "paper" and Play.lower() == "rock":
    print("Player Wins")
elif Player.lower() == "paper" and Play.lower() == "scissors":
    print("Player Loses")
elif Player.lower() == "scissors" and Play.lower() == "rock":
    print("Player Loses")
elif Player.lower() == "scissors" and Play.lower() == "paper":
    print("Player Wins")
else:
    print("Player Provided Invalid Input")