
import string

# this allows for us to loop around
alphabets = string.ascii_lowercase + string.ascii_lowercase

sentence = list(input('enter your text').lower())

instructions = input('enter encrypt, DECRYPT, exit EXIT the program\n'.lower())

shift_size = int(input('enter your shift number: '))

end_program = False 


while not end_program:
    if instructions == 'encrypt':
        for char in range(len(sentence)):
            if sentence[char] == " ":
                sentence[char] = " "
            else :
                new_letter = alphabets.index(sentence[char]) + shift_size
                sentence[char] = alphabets[new_letter]
            #convert list back to a string
        print(''.join(map(str, sentence)))
        end_program = True
    elif instructions == "decrypt":
        #do same thing but backwards
        for char in range((len(sentence))):
            if sentence [char] == ' ':
                sentence[char] = ' '
            else:
                new_letter = alphabets.index(sentence[char]) - shift_size
                sentence[char] = alphabets[new_letter]
                
        print(''.join(map(str, sentence)))
        end_program = True

    else:
        decide = input('invalid entry, try again Y for YES, N for not').lower()
        if decide == 'y':
            sentence = list(input('enter your text').lower())
            instructions = input('enter encrypt, DECRYPT, exit EXIT the program\n'.lower())
            shift_size = int(input('enter your shift number: '))
            
        end_program = False





