import random

class gene():
    def __init__(self):
        self.value = random.randint(0,1)
        pass

class chromosome(gene):
    def __init__(self):
        pass

class DNA(chromosome):
    def __init__(self):
        pass


print(random.randint(0,1))