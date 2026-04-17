#    CODING this was made by me

import random
import string


ms = input("Enter the message: ")
words = ms.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if(coding == "1") else False

def get_random_vlaue():
    return "".join(random.choices(string.ascii_lowercase, k=3))

if(coding):
    neword = []
    for word in words:
      if(len(word)>=3):
        r1 = get_random_vlaue()
        r2 = get_random_vlaue()
        msnew = r1 + word[1:] + word[0] + r2
        neword.append(msnew)
      else:
         neword.append(word[::-1])   
    print(" ".join(neword))     



else:
   neword = []
   for word in words:
     if(len(word)>=9):
       msnew = word[3:-3]
       msnew = msnew[-1] + msnew[:-1]
       neword.append(msnew)
     else:
        neword.append(word[::-1])   
   print(" ".join(neword))     

