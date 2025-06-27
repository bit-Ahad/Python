import os
 
# Read Mode
f = open("FIle  IO/myfile.txt","r")
text = f.read()
print(text)

# Write mode  (w)
# Write new data new data in place of existing data 
f = open("FIle  IO/myfile.txt","w")
f.write("Here is another line using code")

# Append mode (a)
# It add data at the end of existing file 
f = open("FIle  IO/myfile.txt","a")
f.write("Here is another line using code")
f.close()


# Create mode (x)
# Create a file and if already exist gives error 

# Text mode (rt)(wt)
# used for text file

# Binary mode (rb)(wb)
# Used for binary file like images,pdfs

# No need to Close using this syntax
# with open("FIle  IO/myfile.txt","w"):
