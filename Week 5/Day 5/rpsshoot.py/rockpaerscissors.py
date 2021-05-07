from game import Game
# game = Game('rps')




# show main menu, handle user input, and show game summary before exiting 
def get_user_menu_choice():
    user_choice = input("(P)lay Game \n (S)how scores \n (Q)uit\n Select: ").lower()
    valid_presses = ['p', 's', 'q']

    if user_choice not in valid_presses:
        print ("you have now messed up")
        print ("Goodbye")
        # exit()
    return user_choice


def print_results(results):
    print(str(results))

def main():
    while True:
        choice = get_user_menu_choice()
        if choice == 'p':
            print(f'working{choice}')
            game = Game('rps')
            result = game.play()
            # keeping w/l/d record

            if result == 'win':
                results['wins'] += 1
            if result == 'loss':
                results['losses'] += 1
            if result == 'tie':
                results['ties'] += 1
            go_to_menu = input(' Press "enter" to go to menu, "p" play again, Press anything to quit ')
            if go_to_menu == '':
                continue
            if go_to_menu == 'p':
            # need to fix this so it skips the menu
                result = game.play()
                continue
            

            print_results(results)
            break




        if choice == 's':
            print(choice)
            print_results(results)
#             # continue
        if choice == 'q':
            print(f'Bye Bye')
            print_results(results)
            exit()

# record keeper
results = {'wins': 0,'losses': 0,'ties':0}

main()
#show game summary

