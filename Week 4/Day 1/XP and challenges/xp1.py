print ("Hello world\n"*8)

print ((99**3) * 8)

# false
# true
# false
# print ("3" > 3) - error
# false

computer_brand = "MSI"
print (f'I have a(n) {computer_brand} computer')

#  your information
name = "Gregory"
age = 25
shoe_size = 46
info = f'My name is {name}, I\'m {age} , and wear a {shoe_size} shoe. Glad to have this speed date. '
print(info)

#if a is great 6
a = 12
b = 11
if a > b:
    print ("Hello World")

# odd or even 7
number = input("Number ")
number = int(number)

if number % 2 == 0:
    print ("Even")

else: 
    print ("odd")

#my name? 8
my_name = "gregory"
user_name = input("whats your name? ")



if my_name == user_name:
    print ("it'd be funnier if it wasnt my name")
else:
    print ("we are not the same")

height = input("How tall are you in Freedom Units?")
height_cm = int(height)/2.54

if height_cm < 145:
    print ("You're tall enough to ride")

else:
    print ("At least you can still buy kids clothing")