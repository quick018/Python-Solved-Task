import random as r
def start():
    print("Welcome To the Game")
    content = ['snake', 'water', 'gun']

    computer = r.choice(content)
    player = input("Enter the choice: ")

    print("You", player)
    print("Computer", computer)

    if player == "snake" and computer == "water":
       print("Win")
    elif player == "water" and computer == "gun":
       print("Win")
    elif player == "gun" and computer == "snake":
       print("Win")
    elif player == computer:
       print("Draw")
    else:
       print("Lose")    

start()
