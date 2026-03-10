questions1 = ["Which language is used to create game?", "Python", "java", "c++", "javaScript", "None", 3],


levels = [1000, 2000, 3000, 6000, 8000, 12000, 30000, 50000, 80000, 100000, 120000, 140000,]
money1 = 0
for i in range(0, len(questions1)):

  question1 = questions1[i]
  print(f"\n\nWhich language is used to create game Question for RS. {levels[i]}")
  print(f"a. {question1[1]}          b. {question1[2]} ")
  print(f"c. {question1[3]}          d. {question1[4]} ")
  reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))            
  if (reply == 0):
    money1 = levels[i-1]
    break
  if(reply == question1[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
  else:
    print("Wrong Answer.")


questions2 = ["Which language is used to create Web?", "Python", "java", "c++", "javaScript", "None", 1],


levels2 = [50000, 80000, 100000, 120000, 140000,]
money2 = 0
for i in range(0, len(questions2)):

  question2 = questions2[i]
  print(f"\n\nWhich language is used to create Web Question Rs. {levels2[i]}")
  print(f"a. {question2[1]}          b. {question2[2]} ")
  print(f"c. {question2[3]}          d. {question2[4]} ")
  reply2 = int(input("Enter your answer (1-4) or 0 to quit:\n"))            
  if (reply2 == 0):
    money2 = levels2[i-1]
    break
  if(reply2 == question2[-1]):
    print(f"Correct answer, you have won Rs. {levels2[i]}")
  else:
    print("Can Check Again.")


questions3 = ["Which language is used to create old game?", "Python", "java", "c++", "javaScript", "None", 2],


levels3 = [80000, 100000, 120000, 140000,]
money3 = 0
for i in range(0, len(questions3)):

  question3 = questions3[i]
  print(f"\n\nWhich language is used to create old game Question Rs. {levels3[i]}")
  print(f"a. {question3[1]}          b. {question3[2]} ")
  print(f"c. {question3[3]}          d. {question3[4]} ")
  reply3 = int(input("Enter your answer (1-4) or 0 to quit:\n"))           
  if (reply3 == 0):
    money3 = levels3[i-1]
    break
  if(reply3 == question3[-1]):
    print(f"Correct answer, you have won Rs. {levels3[i]}")
  else:
    print("Please Check IT.")
    break  

  


