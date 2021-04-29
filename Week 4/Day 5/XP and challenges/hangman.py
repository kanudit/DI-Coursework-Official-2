import random

wordlist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interfere']
word =random.choice(wordlist)
print(word)
hidden_word = list('*' * len(word))
attempts = 0
# user_attempts = 0
used_letters = []

def gallows_to_print():
    body_parts =["0", "|", "/", "\\", "/", "\\",]
    copy_of_parts = []

    for num in range(attempts):
        copy_of_parts.append(body_parts[num])
    
    while len(copy_of_parts) < 6:
        copy_of_parts.append(" ")


    fgallows = f'''
    |--------
    |     {copy_of_parts[0]}
    |   {copy_of_parts[1]}{copy_of_parts[2]}{copy_of_parts[3]}
    |   {copy_of_parts[4]}  {copy_of_parts[5]}
    '''
    print(fgallows)


def is_valid_guess(text):
        # verify its one letter in alpha
    if len(text) !=1 or not text.isalpha() or text in used_letters:
        return False
        #     return False
        # if not text.isalpha():
        #     return False
        # if text not in used_letters:
        #     return False
    else:
        return True


# PS C:\Users\werk\DI coursework\Week 4\Day 5\XP and challenges>
while attempts < 6:
    if  ''.join(hidden_word) == word:
        #check to make sure he hasnt guessed the complete word
        print('you win!')
        break

    user_input = input('guess a letter: ')
    while not is_valid_guess(user_input):
        print('input invalid')
        user_input = input('guess a letter: ')
        
    if user_input in word:
        print('good guess')
        for index, letter in enumerate(word):
            if letter == user_input: 
                print('replacing letter') 
                hidden_word[index] = letter

# guessed wrong
    else:
        print('bad guess')
        attempts += 1
    print(''.join(hidden_word))
    used_letters.append(user_input)
    print('youve guessed the following letters:', *used_letters)
    print(f'{attempts} /6')
    gallows_to_print()

print('he dead')

