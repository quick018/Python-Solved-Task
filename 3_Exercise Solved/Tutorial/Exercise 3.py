import time
timecheck = time.strftime('%H:')
hour = int(input("Enter the hour: "))

if(hour>=0 and hour<12):
    print("Good Morning Sir:")
elif(hour>= 12 and hour<16):
    print("Good After Noon Sir:")
elif(hour>=16 and hour<19):
    print("Good Evening Sir:")
elif(hour>=19 and hour<24):
    print("Good Night Sir:")
else:
    print("Not Found......")              