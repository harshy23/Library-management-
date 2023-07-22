class library:
    lendbook = {}

    def __init__(self,name,*book):
        self.n=name
        self.b=book

    @property
    def libname(self):
       return f"library name = {self.n}"

    @property
    def displaybooks(self):
        for i in self.b:
            print(i)


    @property
    def addbooks(self):
        n=input("your name=")
        u=input("book you want to give=")
        books.append(u)



    @property
    def lendbooks(self):
        u=input("your name=")
        n=input("name of book=")

        if n not in self.b:
            print("sorry this book is not present")

        elif n in self.lendbook:
            print("this is taken")

        else:
            print("this book is your")
            self.lendbook.update({u:n})


    @property
    def returnbooks(self):

        n=input("your name=")
        print(f"book you have={self.lendbook[n]}")
        u=input("book you want to return=")
        print("thanks for returning")
        del self.lendbook[u]
        books.append(u)
    @property
    def kolo(self):
        print(self.lendbook)




    @property
    def main(self):
        print("press 0 for entry")
        k = int(input())
        if k == 0:
            print(self.libname)
            print("welcome to the library\npress 0 for library name\nprees 1 for seeing all books\nprees 2 for lending a book\npress 3 for adding any book\npress 4 returning book\npress 5 for exiting")

        while(1):
            u=int(input())
            if u==1 :
               print( self.displaybooks)
            elif u==2:
                print(self.lendbooks)

            elif u==3:
                print(self.addbooks)

            elif u==4:
                print(self.returnbooks)

            elif u==5:
                print(self.kolo)

            elif u==6:


                break
            else :
                print("errore")



books=["et","book2","physics","mp","foc","chem"]

harshy=library("harshy",*books)

print(harshy.main)






                                                   ##############