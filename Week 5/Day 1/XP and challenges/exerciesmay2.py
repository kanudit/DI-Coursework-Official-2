# ex 1

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

cat1 = Cat('paco', 3)
cat2 = Cat('Terrel',7 )
cat3 = Cat('Rick', 4)

cats = [cat1, cat2, cat3]

def find_highest_age(cat_list):
    oldest = cat_list[0].age
    for cat in cat_list:
        if cat.age > oldest:
            oldest = cat.age
            print(f'{cat.name} is {oldest}')
find_highest_age(cats)

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f'{self.name} goes woof')

    def jump(self):
        jump_height = self.height *2
        print(f'{self.name} jumps {jump_height}cm')
    
    def details(self):
        print(f'Dave\'s dog is named {self.name} and is {self.height}cm tall ')

davids_dog = Dog("Rex", 50)
sara_dog = Dog("Teacup", 20)
davids_dog.details()

if davids_dog.height > sara_dog.height:
    print(f'Davids dog is bigger')

# ex 3

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven \n"])

stairway.sing_me_a_song()


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        self.animals.append(new_animal)
    
    def get_animals(self):
        print('Subjects Remaining: ')
        print(*self.animals)

    def sell_animal(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'Off to the cage Mr.{animal}')
        else:
            print(f'We already ate the {animal}!!!')

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        print(sorted_animals)




philadelphia = Zoo("philadelphia")
philadelphia.add_animal('tiger')
philadelphia.add_animal('lion')
philadelphia.add_animal('bear')
philadelphia.sell_animal(input('Which innocent soul would you like to profit off of? - '))
philadelphia.get_animals()
philadelphia.sort_animals()




