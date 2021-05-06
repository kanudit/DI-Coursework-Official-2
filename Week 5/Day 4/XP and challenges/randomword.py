def get_words_from_file():
    random_word_file = open('sowpods.txt', 'r')
    wordlist = random_word_file.readlines()
    # file = open('sowpods.txt')
    # random_word_file = file.read()
    # for line in random_word_file:
    #     wordlist.append(line)
    final_wordlist = []
    for word in wordlist:
       new_word = word.replace('\n', '')
       final_wordlist.append(new_word)
    return final_wordlist

import random








def get_random_sentence(length):
    final_wordlist = get_words_from_file()
    sentence_length = length
    random_words = []

    for word in range(length):
        random_words.append(random.choice(final_wordlist))
    # print(random_words)

    print(' '.join(random_words).lower())

# get_random_sentence(10)

length = int(input('put a whole number between 2 and 20'))


if length < 2 or length > 20:
    raise ValueError('That value won\'t work, start again')

get_random_sentence(length)


def main():
    print('This program reads a txt file and will return a random string of words')
main()

# ended up copying lien's code, understand concept couldn't get it though. Practice more

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

my_dict = json.loads(sampleJson)
print("salary = " + str(my_dict['company']['employee']['payable']['salary']))
my_dict['company']['employee']['birth_date'] = None
print(my_dict)

with open('pract.json', 'w') as f:
   json.dump(my_dict, f)