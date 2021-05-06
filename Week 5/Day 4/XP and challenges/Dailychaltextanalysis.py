class Text():
    def __init__(self,text):
        self.text = text
        self.wordbank = self.text.split()

    def frequency(self):

        wanted_word = str(input('put a word: '))
        word_frequency = 0

        for word in self.wordbank:
            if word == wanted_word:
                word_frequency += 1
        # wordfreq = [wordlist.count(word) for word in wordlist]

        print(f'"{wanted_word}" occurs {word_frequency} times')


    def most_common_word(self):
        from collections import Counter

        most_common_word = Counter(self.wordbank)
        most_common_word = most_common_word.most_common(1)
        print("most common word is:")
        print(f'"{most_common_word[0][0]}" is the most common word with {most_common_word[0][1]} occurrences')

    def unique_words(self):
        # wordbank = self.text.split()
        unique_words = []

        for word in self.wordbank:
            if word not in unique_words:
                unique_words.append(word)
        print(*unique_words)            
punc = []
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in punctuations:
    punc.append(i)
print(punc)

import string

class TextModification(Text):
    def __init__(self,text):
        super().__init__(text)





    def remove_punctuation(self):
        print(f"text mod type: {type(self.text)}")
        exclude_chars = set(string.punctuation)
        #removes special characters as well
        self.text = ''.join(char for char in self.text if char not in exclude_chars) 
        print(self.text)
        
    def remove_stop_words(self):    
       
        from nltk.corpus import stopwords 
        from nltk.tokenize import word_tokenize 
        # nltk.download('stopwords')

        stop_words = set(stopwords.words('english'))
        # i feel like this is wrong
        self.text = ''.join(word for word in self.text if word not in stop_words)     
        print(self.text)

poem = Text("It was the day he slept, he slept his last sleep, for he lept his last leap, deep deep into the deep, for what he reap, is what will seep, only for he to keep an electro beep beep.")
# print(poem.text)
story = TextModification("ak , ak, ok, ok")

the_stranger = open("the_stranger.txt", "r")

the_stranger_text = TextModification(the_stranger.read())


# tests
# poem.frequency()
# poem.most_common_word()
# poem.unique_words()
# story.remove_punctuation()

# the_stranger_text.frequency()
# the_stranger_text.most_common_word()
# the_stranger_text.remove_punctuation()
# the_stranger_text.remove_stop_words()