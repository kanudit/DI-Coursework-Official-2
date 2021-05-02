class Farm:
    def __init__(self, farmer):
        self.farmer = farmer
        self.animals = []

    def add_animal(self,new_animal, how_many=1):
        for i in range(how_many):
            self.animals.append(new_animal + ' :')
        # print(self.animals)

    def how_many(self):
        self.animals = {i:self.animals.count(i) for i in self.animals}
        for i in self.animals:
            print(i, self.animals[i])

    def get_animal_types(self):
        types_of_animals = list(dict.fromkeys(self.animals))
        animal_sentence = []
        for animal in types_of_animals:
            new_animal = animal.replace(':','')
            animal_sentence.append(new_animal)
            # print(animal_sentence)
        species = ' '.join(animal_sentence)
        return(species)

    def short_info(self):
        print(f'{self.farmer}\'s farm has at least one of each: a {self.get_animal_types()}')

farm = Farm("mcdonald")
farm.add_animal("Cow", 5)
farm.add_animal("Duck")
farm.add_animal("Duck")
farm.add_animal("Chicken", 3)
print(farm.farmer +"\'s Farm")
farm.how_many()
farm.get_animal_types()

farm.short_info()

# https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list/23240989
# https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
        


    


