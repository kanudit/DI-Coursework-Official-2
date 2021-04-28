# ex1


def display_message(subject):
    return subject
     
topic = display_message(input("input subject: "))
print(f' we are learning {topic} today')

#ex2
def favorite_book(title):
  message =  print(f'my fav book is {title}')
  return message

favorite_book('fahrenheit 451')


# ex3 setting default variable

def describe_city(city, country = "yomommas house"):
    print(f'{city} is a city in {country}')

describe_city("qwer")

#ex 4
import random

def same_number_checker (a):
    if 1 < a < 100:
        b = random.randint(1, 100)
        if a == b: 
            print(f'Success')
        print(f'Fail {a} doesnt equal {b}')

same_number_checker(12)


# ex5 shirt texxt picker

def make_shirt(size = "large", shirt_text = "I love Python"):
    if size == "large" or "medium":
        shirt_text = shirt_text
    shirt_text = "heyyyyyy"
    print(f'Shirt Size: {size}, Shirt Text: {shirt_text}')

make_shirt("small")

# ex 6
magician_names = ["Joe", "Harry", "Taco", "Guy", "Darnell"]

def show_magicians(list_of_names):
    for name in magician_names:
        print(name)
show_magicians(magician_names)

def make_great(list_of_names):
    index_counter = 0
    for name in magician_names:
        
        great_name = "the great " + name
        magician_names[index_counter] = great_name
        index_counter += 1
    print(magician_names)

make_great(magician_names)





