import time

# Delay for 2 second
# print("Sleeping for 2 seconds...")
# time.sleep(2)
# print("Awake now!")

# Gives local time
F = time.localtime()
g = time.strftime("%H:%M:%S", F)
print("Local time is : ",g)

# Formated Time
print(time.strftime("%Y-%m-%d"))

# give second passed after 1970
# print(time.time())