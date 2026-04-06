import random as r

def check(pc, player):
    if pc == player:
       return 0
    if(pc == 0 and player == 1):
       return -1
    if(pc == 1 and player == 2):
       return -1
    if(pc == 2 and player == 0):
       return -1
  
    return 1

pc = r.randint(0, 2)
player = int(input("0 for snake, 1 for water, 2 for gun: "))

score = check(pc, player)
print("Your", player )
print("Computer", pc)

if(score == 0):
  print("Draw")
elif(score == -1):
  print("Lose")
else:
  print("Win")    