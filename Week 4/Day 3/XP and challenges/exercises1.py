# # exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionary = dict(zip(keys, values))
# print(dictionary) # {'a': 1, 'b': 2, 'c': 3}


# # # exercise 2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# total_cost = 0

# for name,age in family.items():
    
#     if age  < 3:
#         ticket_price = 0
#         print(f'{name} pays: ${ticket_price}')

#     elif 3 < age < 12:
#         ticket_price = 10
#         total_cost += ticket_price
#         print(f'{name} pays: ${ticket_price}')

#     else:
#         ticket_price = 15
#         total_cost += ticket_price
#         print(f'{name} pays: ${ticket_price}')


# print(f'Please enjoy your movie but only after paying: ${total_cost}')

#exercise 3

brand = {'name': "Zara" ,
'creation_date': 1975 ,
'creator_name': "Amancio Ortega Gaona" ,
'type_of_clothes': ["men", "women", "children", "home"], 
'international_competitors': ["Gap", "H&M", "Benetton"],
'number_stores': 7000 ,
'major_color' : {
    'France': "blue", 
    'Spain': "red", 
    'US': ["pink", "green"]}
}

brand['number_stores']=2

brand['country_creation'] = 'Spain'

print(brand['number_stores'])
print("We serve:" + " ".join(brand['type_of_clothes']))

if "international_competitors" in brand:
    brand['international_competitors'].append("desiglia")

# if 'creation_date' in brand:
del(brand['creation_date'])

print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(brand.keys())

more_on_zara = {
'creation_date': 1975, 
'number_stores': 10000,
}

new_zara = brand | more_on_zara

# print(new_zara)

brand.update(more_on_zara)

# print(brand)


#ex 4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]


disney_users_a = {}


for index, user in enumerate(users):
    disney_users_a[user] = index

     
print(disney_users_a)

    #  add number to  user
    #  add user to disney_users_a
      
    #  enumarte give positon ur at and value 
    # print(user)




