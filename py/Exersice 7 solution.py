import os

files = os.listdir(r"A:\Codes\py")

i = 1
for file in files:
    if file.endswith(".png"):
        print("PNG file deteccted. ")
        os.rename(file, f"{i}.png")
        i+=1