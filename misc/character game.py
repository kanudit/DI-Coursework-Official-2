class Character():
    def __init__(self,name, life = 20, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
        if self.name == 'scrub':
            print('I\'m just a scrub')
    
    def basic_attack(self, other_character):
        other_character.life -= self.attack

class Druid (Character):
    def __init__(self,name,life = 20, attack = 10):
        super().__init__(name, life, attack)
        print(f'{self.name} the Druid Here')

    def meditate(self):
        self.life += 10
        self.attack -= 2
    
    def animal_help(self):
        self.attack += 5

    def fight(self,other):
        other.life -= (0.75*self.life + 0.75 * self.attack)
        print(f'{self.name} used Fight on {other.name} \n doing {(0.75*self.life + 0.75 * self.attack)} damage \n {other.name} has {other.life} health left')



class Warrior (Character):
    def __init__(self,name,life = 20, attack = 10):
        super().__init__(name, life, attack)
        print(f'{self.name} the Warrior Here')

    def brawl(self,other):
        other.life -= (2*self.attack)
        self.life += (0.5*self.attack)
        print(f'{self.name} used Brawl on {other.name} \n doing {(2*self.attack)} damage \n {other.name} has {other.life} health left')


    def train(self):
        self.attack += 2
        self.life += 2
    def roar(self,other):
        other.attack -= 3

    

class Mage (Character):
    def __init__(self,name,life = 20, attack = 10):
        super().__init__(name, life, attack)
        print(f'{self.name} the Mage Here')

    def cast_spell(self,other):
        other.life -= (self.attack/self.life)
        print(f'{self.name} used Cast Spell on {other.name} \n doing {self.attack/self.life} damage \n {other.name} has {other.life} health left')

    def summon(self):
        self.attack += 3
        
    def curse(self,other):
        other.attack -= 2
    pass

scrub = Character('scrub')
pogo = Druid('Pogo')
dilby = Warrior('Dilby')
booger = Mage('booger')

booger.cast_spell(dilby)
pogo.fight(booger)
dilby.brawl(pogo)
# print(scrub.name)

# pogo.meditate()
# print(pogo.life)
# pogo.basic_attack(scrub)
# print(scrub.life)
# pogo.animal_help
# pogo.fight(scrub)
# print(scrub.life)