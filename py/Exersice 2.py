import time
t = int(time.strftime('%H'))
print("Hour",t)
if(t>=0 and t<12):
    print("Good Morning Sir")
elif(t>=12 and t<16):
    print("Good Afternoon Sir")
elif(t>=16 and t<24):
    print("Good Evening Sir")

# It used time module it is built in 
print(time.strftime('%M')) #For Minutes
print(time.strftime('%S')) #For Seconds