questions = [
  [
    "Which language is used for gaming industries?", "Python", "Javascript", "c#", "none", 3 
  ],
  [
   "Which language is used for gaming industries?", "Python", "Javascript", "c#", "none", 3 
  ],
  [
    "Which language is used for gaming industries?", "Python", "Javascript", "c#", "none", 3 
  ],
  [
    "Which language is used for gaming industries?", "Python", "Javascript", "c#", "none", 3 
  ],
]

levels = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
money = 0
for i in range(0,len(questions)):
  
  question = questions[i]
  print(f"\n\nWhich language is used for gaming industries? Question for RS. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]}")
  print(f"c. {question[3]}          b. {question[4]}")

  reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
  if(reply == 0):
    money = levels[i-1]
    break
  if(reply == question [-1]):
    print(f"Correct answer, you have won RS.{levels[i]}")
    break  
  else:
    print("Wrong answer")  
    # break
 