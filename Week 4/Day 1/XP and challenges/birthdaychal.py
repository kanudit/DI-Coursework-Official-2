import datetime

birthday = input('enter birthday dd/mm/yyyy')
new = birthday.split('/')
print(new)


birth_year = int(new[-1])
print(birth_year)
current_year = 2021

age = current_year - birth_year
print(age)

decades = int(age/10)


if decades < 1:
    decades = 1
# if decades > 5:
#     decades = 5

print(decades)

spaces = 3

i_line = (f' ' * spaces + '__' '|' + 'i' * decades + '|__')
happy_line = (f'  |:H:a:p:p:y:|')
second_top = (f'__|' + '_' * 11 + '|__')
icing = (f'|' + '^' * 18 + '|')
birthday = (f'|:B:i:r:t:h:d:a:y|')
spaces = (f'|' + ' ' * 16 + '|')
baseline = (f'~' *20)

if decades > 5:
    i_line = (f'you\'re to old for me to figure this out')


print(i_line)
print(happy_line)
print(second_top)
print(birthday)
print(spaces)
print(baseline)


#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
