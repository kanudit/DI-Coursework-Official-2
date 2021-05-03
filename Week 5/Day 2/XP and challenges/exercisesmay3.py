class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Paulie(Cat):
    def sing(self, sounds):
        return f'{sounds}'


taco = Bengal("Taco", 11)
kalo = Paulie("Kalo", 4)
razer = Chartreux("Razer", 1)
paulie = Paulie("Bill", 5)

my_cats = [taco, kalo,razer, paulie]
my_pets = Pets(my_cats)
my_pets.walk()

class Dog():
    def __init__(self, name, age , weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    
    def run_speed(self):
       run_speed = self.weight /self.age * 10
       return run_speed

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            print (f' {self.name} beat {other_dog.name}')


lev = Dog("lev",2,25)
levi = Dog("levi",3,22)
lucky = Dog("lucky",5,30)
lev.fight(lucky)

