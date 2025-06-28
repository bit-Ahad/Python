word = input("Enter any word : ")
if len(word)>3:
    r1 = "hes"
    r2 = "fwv"
    word = r1 + word[1:]+word[0] + r2
    print("Secret Code is : ",word)
else:
    word = word[::-1]
    print("Secret Code is : ",word)

word = input("Enter any word : ")
if len(word)>3:
    word = word[3:-3]
    word = word[len(word)-1] + word[:-1]
    print("Decoded form of word is : ",word)
else:
    word = word[::-1]
    print("Decoded form of word is : ",word)