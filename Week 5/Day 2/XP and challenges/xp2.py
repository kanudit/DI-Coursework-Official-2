# family exercise

class Family():
    def __init__(self):
        self.members =  [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        self.last_name = "bergerstein"

    def born(self, **kwargs):
        newborn = {'name':'titty','age':0,'gender':'Female','is_child':True}
        newborn['name'] = kwargs['name']
        newborn['gender'] = kwargs['gender']
        nbgender = 'girl'

        if newborn['gender'] == 'Male':
            nbgender = 'boy'
        print (f'Congrat on the new baby {nbgender}, {newborn["name"]}')

        # self.members = self.members.copy()
        self.members.append(newborn)


    def is_18(self, name):
        for person in self.members:
            if person['name'] == name:
                if person['age'] < 18:
                    print (f' {person["name"]} a child? {person["is_child"]}')
    
    def full_family(self):
        for person in self.members:
            print (f' {person["name"]} is a {person["gender"]} human that is {person["age"]} years of age.')
        



# bergerstein = Family()
# # print(bergerstein)
# bergerstein.born(name='Darnell', gender='Male')
# bergerstein.is_18('Darnell')
# bergerstein.full_family()



class TheIncredibles(Family):
    def __init__(self):
        self.members =[
            {'name':'Dad','age':40,'gender':'Male', 'power':'strength'},
            {'name':'Mom','age':39, 'gender':'Female','power':'stretch'}
        ]

    def use_power(self):
        for member in self.members:
            try:
                if member['age'] > 18 :
                    print(f' {member["name"]} used {member["power"]}')
            except:
                print(f' {member["name"]} is too young to use {member["power"]}')
    def present_family(self):
        for member in self.members:
            try:
             print(f' {member["name"]} uses her power:{member["power"]}')
            except KeyError:
                if member['name'] == 'Violet':
                    print(f' {member["name"]} uses invisibility')
                if member['name'] == 'Boy':
                    print(f' {member["name"]} uses speed')



incredibles = TheIncredibles()
incredibles.born(name='Violet', age=16, gender='Female', power="invisible")
incredibles.born(name='Boy', age=12, gender='Male', power="speed")
incredibles.use_power()
incredibles.present_family()

