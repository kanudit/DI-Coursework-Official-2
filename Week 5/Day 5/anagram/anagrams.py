from anagram_checker import AnagramChecker

def user_menu():
    # show menu and dont stop until exited
    while True:
        word_choice = input("enter a 'word' or 'exit' to exit - ")
        item_list = word_choice.split()
        if len(item_list) > 1:
            print("too many words")
            continue    
        for item in item_list:

            if item.isalnum() == False:
                print("isn't a word")
                continue
                 
            if item == 'exit':
                print("Goodbye (exit has no anagrams)")
                exit()

        anagram = AnagramChecker("sowpods.txt")
        # returns the anagram list
        user_anagrams = anagram.get_anagrams(word_choice)
        if user_anagrams == []:
            user_anagrams = f'"there are no anagrams for {word_choice}"'
        print(f'The anagrams for "{word_choice}" are in the following list:\n {user_anagrams}')
user_menu()

        


        # item_checker = []
        
        #     item_checker.append(string)
       
            
        # if word_choice == "`":
        #     break



# anagram = AnagramChecker("sowpods.txt")
# word = anagram.is_valid_word()
# anagram.get_anagrams(word)