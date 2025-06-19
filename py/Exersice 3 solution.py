score = 0
q = [ ["What is answer of question 1 : ",1,1,1,1]
, ["What is answer of question 2 : ",2,2,2,2]
, ["What is answer of question 3 : ",3,3,3,3]
, ["What is answer of question 4 : ",4,4,4,4]
]

# Exersice needs sets or list of list

for i in range(len(q)):
    print(q[i][0],"\n")
    print("a : ",q[i][1],"\t\tb : ",q[i][2],"\nc : ",q[i][3],"\t\td : ",q[i][4])
    ans = int(input("Enter your answer : "))
    if(i==0):
        if(ans==1):
            print("Correct Answer")
            score = score + 100
        else:
            print("Wrong Answer !")
            break
    elif(i==1):
        if(ans==2):
            print("Correct Answer")
            score = score + 100
        else:
            print("Wrong Answer !")
            break
    elif(i==2):
        if(ans==3):
            print("Correct Answer")
            score = score + 100
        else:
            print("Wrong Answer !")
            break
    if(i==3):
        if(ans==4):
            print("Correct Answer")
            score = score + 100
        else:
            print("Wrong Answer !")
            break

print("Better Luck next time")
print("Your score is : ",score)