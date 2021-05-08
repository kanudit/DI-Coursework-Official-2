# What is a class?
# a class provides the skeleton/blueprint for a group of object

# What is an instance?
#  An instance is an occurence of an object. 

# What is encapsulation?
# Encapsulation is the creation of a 'barrier' so that
#  data within a unit (instance of a class) can only be edited from within the unit preventing changes fromm the outside.


# What is abstraction?
# Abstraction is providing only the esssential info/functionality,
# without giving 'how it all works'

# What is inheritance?
# Inheritance is the characteristic of classes to be able to take on the properties and method of other classes

# What is multiple inheritance?
# This is the ability to inherit traits from multiple classes of varying parent levels 

# What is polymorphism?
# polymorphism allows us to use the same function on different data and data types. 
# Such as using the same function to find the area of a square and a triangle

# What is method resolution order or MRO?
# Mro is the order that a class uses methods from its parent classes.



# this exercise doesn't make sense. Why would a deck inherit from it's card? They are unrelated. If anything a deck would determine the characteristics of its cards.
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades' ]
values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]



class Card():
    def __init__(self, suit,value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print(f' {self.value} of {self.suit}')


class Deck(Card):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

