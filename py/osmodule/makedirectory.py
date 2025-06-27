import os

#if (not os.path.exists("Ahad")):
    #os.mkdir("Ahad")

if (not os.path.exists("os module/Testing")):
    for i in range(1,6):
      os.mkdir(f"os module/Testing/File{i}")

print(os.listdir("os module\Testing"))

folders = os.listdir("os module/Testing")
for folder in folders:
   print(folder)
   print(os.listdir(f"os module/Testing/{folder}"))

# Give name of current directory
print(os.getcwd())
# It change directory
os.chdir("os module/Testing")
print(os.getcwd())
