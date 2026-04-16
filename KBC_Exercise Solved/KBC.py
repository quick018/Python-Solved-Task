name = input("What's Your Name: ")
welcome = ("You are Welcome")
print(f"{welcome} {name}")

Questions = ["Which language is most used for gaming industries?", 'Python', 'JavaScript', 'c#', 'c++', 4],
levels = [10000,20000,40000,60000,80000,100000,]
Money = 0

def info():
    print("......Thanks For Coming in KBC......")

for i in range(0,len(levels)):
    
    question = Questions[i]
    print(f"Which language is most used for gaming industries?, ")
    print(f"a.  {question[1]}  b.  {question[2]}")
    print(f"c.  {question[3]}      d.  {question[4]}")

    reply = int(input("Enter your answer: "))
    if(reply == levels [i-0]):
        print("You lose")
        break
    if(reply == question [-1]):
        print(f"Correct answer you won Rs. {levels[i]} {name}")    
        break
    else:
        print(f"Wrong answer {name}")
        break

info()