# CODING

txt = input("Enter the txt: ")
words = txt.split(" ")
coding = input("1 For Coding or 0 For Decoding: ")
coding = True if(coding == "1") else False

if(coding):
    txtword = []
    for word in words:
      if(len(word)>=3):
        a1 = "opp"
        a2 = "roc"
        txtnew = a1 + word[1:] + word[0] + a2
        # print(txtnew)
        txtword.append(txtnew)
      else:
         txtword.append(word[::-1])
    print(" ".join(txtword))

# Decoding

else:
    txtword = []
    for word in words:
      if(len(word)>=3):
        txtnew = word[3:-3]
        txtnew = txtnew[-1] + txtnew[:-1]
        # print(txtnew)
        txtword.append(txtnew)
      else:
         txtword.append(word[::-1])
    print(" ".join(txtword))

        