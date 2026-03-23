#    CODING this was made by me

ms = input("Enter the message: ")
words = ms.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if(coding == "1") else False
if(coding):
    neword = []
    for word in words:
      if(len(word)>=3):
        r1 = "opp"
        r2 = "miu"
        msnew = r1 + word[1:] + word[0] + r2
        neword.append(msnew)
      else:
         neword.append(word[::-1])   
    print(" ".join(neword))     



else:
   neword = []
   for word in words:
     if(len(word)>=3):
       msnew = word[3:-3]
       msnew = msnew[-1] + msnew[:-1]
       neword.append(msnew)
     else:
        neword.append(word[::-1])   
   print(" ".join(neword))     

