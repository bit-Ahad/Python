# Make Using snake water Game
# Matrix of win is Given In VIdeo

import random as r

sel = [1,2,3]
name = ["Snake","Water","Gun"]
win = [
    ["Draw" , "Win" , "Lose"],["Lose" , "Draw" , "Win"],["Win" , "Lose" , "Draw"]
]
while True:
    comp = r.choice(sel)
    # print(comp)

    play = int(input("\nSelect one of following:  \n1 for Snake \n2 for Water \n3 for Gun\n"))
    while(play!=1 and play!=2 and play!=3):
        play = int(input("Enter only from 1 2 3 : "))
    else:
        if (play==1):
            print("\nYou Selected : ",name[0])
        elif (play==2):
            print("\nYou Selected : ",name[1])
        elif (play==3):
            print("\nYou Selected : ",name[2])

    if (comp==1):
        print("\nComp Selected : ",name[0])
    if (comp==2):
        print("\nComp Selected : ",name[1])
    if (comp==3):
        print("\nComp Selected : ",name[2])

    print("\nResult is : You",win[play-1][comp-1])
    end = int(input("Enter 0 if you want to exit Or Enter 1 if you want to play again : "))
    if(end==0):
        break

print("\nThanks for playing game .......")