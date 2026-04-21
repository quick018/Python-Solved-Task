# Quick Quiz: Implement a Cat class by using the animal class. 
# Add some methods specific to cat

  # this quiz made by me

class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space

    def make_sound(self):
        print("This sound was made by animal")

    def make_legs(self):
        print("4 Legs")

class Cat(Animal):
    def __init__(self, name, gread):
        Animal.__init__(self, name, space="Cat")     
        self.gread = gread 

    def make_sound(self):
        print("Meow")

    def make_count(self):
        print("This is Cat")              

al = Animal("Cat", "Dog")
al.make_sound()
al.make_legs()

al2 = Cat("Rat", "Mat")
al2.make_sound()        
al2.make_count()        