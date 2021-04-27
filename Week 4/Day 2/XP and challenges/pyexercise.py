# numbers = [2,2,5,6,6,4,4,8,9,1]

# print(set(numbers))

# uniquenumbers = set(numbers)

# other_numbers = {8,5,4,7,8,8,5,2,3,6}




# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# print(school.difference(attendance_list))
# # attendance_list = set(attendance_list)


# list1 = [5,10,15,20,25,50,20]

# wanted_index = list1.index(20)
# list1[wanted_index] = 200 



# print(list1)


# oneten = 0

# while oneten < 10:
#     oneten += 1
#     print(oneten)
# print('boom')

# # ----------------------------------
# # ex1

# my_fav_numbers = {1,2}
# my_fav_numbers = list(my_fav_numbers)


# my_fav_numbers.remove(my_fav_numbers[-1])

# print(my_fav_numbers)

# friend_fav_numbers = {5,9,6}
# print(friend_fav_numbers)
# friend_fav_numbers = list(friend_fav_numbers)
# print(friend_fav_numbers)


# our_fav_numbers = my_fav_numbers + friend_fav_numbers
# print(set(our_fav_numbers))

# # ---------------
# # ex 2

# # Yes, but only once. Tuples can only contain unique numbers
# # ---------------
# #  ex 3  Exercise 3: Print A Range Of Numbers


# numbers = 1

# while numbers < 21:
#     print(numbers)
#     numbers += 1


# # ---------------
# # ex 4
# # a float has a decimal and isn't always a whole number. Integers are whole numbers
# # ---------------

# start = 1.5
# jumper = .5
# array = []

# while start < 5.5:
#     print(start)
#     array.append(start)
#     start += jumper
# print(array)

# # ----------------------
# # ex5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")

# how_many_apples = basket.count("Apples")
# print(f'Number of apples: {how_many_apples}')
# basket.clear()
# print(basket)


# # --------------
# # ex 6
# name = input("Put your name: ")

# while name != "greg":
#     print("try again")
#     name = input("")
# print("cool name")


# #-----------
# # ex 7
# start_num = 0
# my_list = []

# while start_num < 26:
#     my_list.append(start_num)
#     start_num += 1
    
# print(my_list)

# for i in my_list:
#     if my_list.index(i) % 2 == 0:
#         print(my_list[i])
# --------
# # eex  8
# # Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
# # wording of question is confusing

# number_range = range(1500,2500)

# for number in number_range:
#     if number % 5 == 0 and number % 7 == 0:
#         print(number)

# # ------
# ex 9


user_fruits = input("put your fav fruits in seperated by a space: ")
fav_fruits = user_fruits.split()
fruit_pick = input("pick a fruit")

while True:
    if fruit_pick in fav_fruits:
        print("nice pick, thats my fave")
        break
    fruit_pick = input("pick a fruit")



    print("wow u pick a favorite")

#ex10
pizza_price = 10 
pizza_topping= input("what topping do you want?")
toppings=[]

while True:
    if pizza_topping != "quit":
        toppings.append(pizza_topping)
    print(len(toppings) * 2.5 + pizza_price)
     



# ex 11
ask_customer_ages = input("enter age seperated by a space")
# ask_customer_ages = int(ask_customer_ages)
age_split = ask_customer_ages.split()
age_map = map(int,age_split)
age_list = list(age_map)

print(age_list)

total_cost = 0

for age in age_list:
    if age  < 3:
        ticket_price = 0
    elif 3 < age < 12:
        ticket_price = 10
        total_cost += ticket_price
    else:
        ticket_price = 15
        total_cost += ticket_price
print(f'Please enjoy your movie but only after paying: ${total_cost}')

# change list of strings to list of int
ask_teen_ages = input("enter age seperated by a space")
# ask_customer_ages = int(ask_customer_ages)
age_split = ask_teen_ages.split()
age_map = map(int,age_split)
teen_list = list(age_map)

print(teen_list)

total_cost = 0
permitted_teens = []

for age in teen_list:
    if 16 < age < 21:
        permitted_teens.append(age)
print(f'user with these ages are permitted: {permitted_teens} ')

# for teen in permitted_teens:??
    
# -------------

# ex 13
sandwich_orders =["roast beef","pastrami","pastrami","pastrami","tuna melt", "cheesesteak", "taco delight"]
print("we are out of pastrami mami")

pastrami = "pastrami"
finished_sandwiches =[]


while pastrami in sandwich_orders:

    sandwich_orders.remove(pastrami)

print(sandwich_orders)

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'sandwich with {sandwich}')
