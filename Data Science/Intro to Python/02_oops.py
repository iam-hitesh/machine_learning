class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = 'Mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


mydog = Dog('Lab',"Tommy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)



# class Dog():
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name


# mydog = Dog(breed='Lab',name="Tommy")
# print(mydog.breed)
# print(mydog.name)


# class Dog():
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name


# mydog = Dog('Lab',"Tommy")
# print(mydog.breed)
# print(mydog.name)
