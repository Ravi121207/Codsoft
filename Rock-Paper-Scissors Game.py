import random

while True:

    print("\n")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    selection = int(input("Enter The Choice: "))
    
    if (selection == 1):
        player = "Rock"
    elif (selection == 2):
        player = "Paper"
    else:
        player = "Scissors"
    
    print("\n")
    print("Player ", player)

    game = ["Rock", "Paper", "Scissors"]
    throw = random.choice(game)

    print("Game throws", throw)
    
    if (player == throw):
        print("Tie Game!")
    elif (player == "Rock"):
        if (throw == "Paper"):
            print("Wins!")
        elif (throw == "Scissors"):
            print("Player Wins!")
    elif (player == "Paper"):
        if (throw == "Scissors"):
            print("Wins!")
        elif (throw == "Rock"):
            print("Player Wins!")
    elif (player == "Scissors"):
        if (throw == "Rock"):
            print("Wins!")
        elif (throw == "Paper"):
            print("Player Wins!")
    
    print("\n")
    print("1) Play Again")
    print("2) Quit")
    selection = int(input("Enter Choice: "))
    
    if (selection == 2):
        break