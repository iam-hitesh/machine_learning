#INHERITANCE

class Animal():

    def __init__(self):
        print("Animal Class Created")

    def whoami(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal): #Passing Whole Class to Dog Class

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self,name):
        print("Woof")
        print(name)

    def dogEat(self,whattoeat):
        print("My Dog eats " + whattoeat)



# Now we don't need to call Animal class , we can use Animal class directly from the Dog class


animal = Dog()
animal.whoami()
animal.eat()
animal.bark(name = 'Tommy')
animal.dogEat(whattoeat = 'biscuit')



#SPECIAL METHODS

class Book():


    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title : {},Author:{},Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A Book is Deleted")


b = Book('Intro to Python','Hitesh Yadav',320)
print(b)
print(len(b))
del(b)
