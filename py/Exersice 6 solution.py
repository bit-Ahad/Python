class library:
    def __init__(self):
        self.book = []
        self.num = 0
    
    def addbook(self):
        while True:
            self.num += 1             
            add = input("Enter a book name  :  ")
            self.book.append(add)
            choice = int(input("Enter 1 to add more book or press 0 to exit  :  "))
            try :
                if(choice==0):
                    print("Number of books is : ",self.num)
                    break
                elif(choice==1):
                    continue
                else:
                    print("Enter Correct from 1 and 0  :  ")
            except:
                raise ValueError("Invalid Input. Enter Correct value...................")
    
    def print(self):
        for b in self.book:
            print(b)

li1 = library()
li1.addbook()
li1.print()
