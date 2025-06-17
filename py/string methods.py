a = "Ahad"
print(len(a))           #Lenght
print(a.upper())        #Uppercase
print(a.lower())        #Lowercase
print(a.center(72))     #Total lenght become 72 with spaces in start
b = "You are are very good man"
print(b.split())        #It covert the string into list
print(b.count("are"))   #It cout total occurance
print(b.find("good"))   #It give index of first occurance
print(b.index("good"))  #It is same as find but give error it not found and program close
c = "Ahad!!!!!"
print(c.endswith("!!!")) #It check if end with given string
print(c.rstrip("!"))    #It removes given from last
d = "HeLLo BroTher"
print(d.capitalize())    #Make first letter captial rest small
e = "Ac24sfsff7943"
print(e.isalnum())        #It check if string consist of only alphabets and numeric characters
print(e.isalpha())        #It check if string consist of only alphabets characters
print(e.isdecimal())      #It check if string consist of Decimas characters
f = "ajsdis"
print(f.islower())        #It check if it consist of only lower case letters
print(f.isupper())        #It check if it consist of only upper case letters
g = "\n\n\n It is not printable"
print(g.isprintable())    # \n is not printable
h = "         "           #It consist of white spaces usig spacebar
i = "   "                 #It consist of white space using tab space
print(h.isspace())
print(i.isspace())
j = "PYTHON is good"
print(j.replace("PYTHON","Good"))
print(j.startswith("PYTHON"))   #It check if it start with given word
print(j.swapcase())             #It change upper case into lower case and vice versa
print(j.title())                #Convert first letter of each word captial