# Daily Challenge
import random

string = input("enter 10 characters: ")
while len(string) != 10:
    print("doesnt work")
    string = input("try again with 10 characters")

# print(working_string)

print("first character: " + string[0])
print("last character: " + string[-1])
print(string + "\n")

#don't forget to make your new string 
phrase =''

for letter in string:
    phrase += letter 
    print(phrase)

print(phrase)

shuffled_phrase = ''.join(random.sample(string, len(string)))
print("shuffle Phrase "+ " " + shuffled_phrase)

#raz was a balla here