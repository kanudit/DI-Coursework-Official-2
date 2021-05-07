from itertools import permutations

class AnagramChecker():
    def __init__(self,text_file):
        with open(text_file, 'r') as inputfile:
            self.content = (inputfile.read())
            # clean_content = self.content.replace('\n','')
            self.content_list = self.content.split('\n')
            self.lower_content = []
            for item in self.content_list:
                word = item.lower()
                self.lower_content.append(word)

            # for word in clean_contesadnt:  
            #    content_list.append(word)
            # print(('loaded'))
            # print (self.lower_content)
    
    def is_valid_word(self,word):
        ''' checks if given word is valid '''
        if word in self.lower_content:
            return True
        False
        
    
    def get_anagrams(self,word):
        
        letter_permutations = [''.join(p) for p in permutations(word)]
        permutation_set = set(letter_permutations)
        # checking if items of the permutation is in word bank
        anagrams = [combo for combo in permutation_set if combo in self.lower_content]
        # take out word
        try:
            anagrams.remove(word)
        # print(anagrams)
        finally:
            return anagrams

        # check the given word, jumble it up and for each jumbled up word check 
        # it against the lower_content list
        # if it exists add it to anangrams.

        
    # def is_anagram(word1, word2):
    #     ''' returns true if words have same letters 
    #     but not in the same order
    #     otherwise returns false'''
    #     pass

