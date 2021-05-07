import random

class Game():
    def __init__(self,game_name):
        self.game_name = game_name
        self.items = ['rock', 'paper', 'scissors']
        self.cmds = ['exit'] 
    

    def get_user_item(self):
        user_pick = str(input('pick : rock,paper or scissors - '))
        # if user_pick == 'exit':
        #     exit()
        while user_pick not in self.items and user_pick not in self.cmds :
                print('pick: rock paper scissors')
                user_pick = str(input('pick : rock,paper or scissors - '))
        return user_pick
 

    def get_computer_item(self):
        comp_item = random.choice(self.items)
        print(f' get_computer_item() = you\'ve chosen {comp_item}')

        return comp_item

    # user_item = get_user_item()
    # computer_item = self.get_computer_item()


    def get_game_result(self , user_item, computer_item):
        # user_item =   self.get_user_item()
        # computer_item = self.get_computer_item()
        tie = 'tie'
        win = 'win'
        loss = 'loss'

        if user_item == computer_item:
            return tie
            

        elif user_item == 'rock':
            if computer_item == 'scissors':
                return win
            return loss
            
        elif user_item == 'paper':
            if computer_item == 'scissors':
                return loss
            return win

        elif user_item == 'scissors':
            if computer_item == 'rock':
                return loss

            return win
        
        
        print(f'wins: {self.wins} losses: {self.losses}  ties: {self.ties}')
        (self.losses)
        (self.ties)


    def play (self):
        user_item = self.get_user_item()
        if user_item in self.cmds:
            return user_item
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item,computer_item)
        print(f' you selected: {user_item} the computer selected: {computer_item} \n You {result}')
        return result

     

# game = Game('rps')
# print(game.game_name)
# game.get_user_item()
# game.get_computer_item()
# game.get_game_result()