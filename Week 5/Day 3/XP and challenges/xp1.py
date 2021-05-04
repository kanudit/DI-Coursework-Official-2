# def print_thing(thing):

#     ''' This is going to give you the absolute value, integer value, and input of your thing'''
#     print(abs(thing))
#     print(int(thing))
#     print(input(thing))
#     print(print_thing.__doc__)
    
# red = 4

# print_thing(red)



class Currency():
    def __init__(self, coin_name, amount):
        self.coin_name = coin_name
        self.amount = int(amount)
        
    def __str__(self):
        return (f'{self.amount} {self.coin_name}')


    def __repr__(self):
        return f'currency: {self.amount}\namount: {self.coin_name}'
        
    
    def __int__(self):
        return int(self.amount)

    def __add__(self, other):

        if type(other) == int:
            return self.amount + other

        elif self.coin_name == other.coin_name:
    
            return self.amount + other.amount
        else:
            print(f'TypeError: Cannot add two types of coins')


        # return self.amount + other 
    # def __add__(self, other):
        
    #     if self.coin_name == other.coin_name:
    #         return (f'{self.amount + other.amount} {self.coin_name}')
        
    #     else:
    #         return TypeError((f'cannot add two types of currencies'))4

    def __iadd__(self,other):
        if type(other) == int:
            self.amount = self.amount + other
            return self
        elif self.coin_name == other.coin_name:
            self.amount = self.amount + other.amount
            return self
        else:
            print(f'TypeError: Cannot add two types of coins')

        




c1 = Currency('Dollars',5)
c2 = Currency('Dollars', 10)
c3 = Currency('Yen',1)
c4 = Currency('Yen',10)

# print(str(c1))

# print(int(c1))

# print(repr(c1))
# c1 +5 is c1.amount + 5

print(c1 + 5)
c1 += 5


