import random

def check(computer, player):
    if computer == player:
        return 0

    if computer == 1 and player == 2:
        return -1    
    if computer == 0 and player == 1:
        return -1
    if computer == 2 and player == 0:
        return -1
    
    return 1
    
computer = random.randint(0, 2)    
player = int(input("0 for snake, 1 for water, 2 for gun:\n"))

score = check(computer, player)

print("You", player)
print("Computer", computer)

if(score == 0):
    print("It's Draw")
elif(score == -1):
    print("Lose")
else:
    print("You Won")        
