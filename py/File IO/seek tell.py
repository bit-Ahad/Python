import os
if not os.path.exists("Ahad.txt"):
    a = open ("Ahad.txt","w")
    a.write("sadasdsadsad is here writng si fnjaf sja s ahu sh hs hd hs dh saj dhjsa dh hj jh  gh    kjgjk gjhjhgjgjgjj hkjhkjh")
    a.close()

a = open ("Ahad.txt","r")

# seek() skip first 17 bytes of file
a.seek(17)
data = a.read()
print(data)

# tell() It will tell the position from where the reading will start
teller = a.tell()
print(teller)

#truncate() change the size of file to 5 bytes
# a.truncate(5)
# It is used while writing 