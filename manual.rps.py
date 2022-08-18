
import random

class RockPaper:

    def __init__(self):
        self.choices = [' rock', 'paper', 'scissors']
        

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice
    

    def get_user_choice(self):
        user_choice = input(" Please choose Rock, Paper, or Scissors ").lower()
        return user_choice 
           
        
    def get_winner(self, computer_choice, user_choice):

        print(f" You've chosen {self.user_choice}. The computer chose {self.computer_choice} ")
            
        if self.computer_choice  == 'rock':
            if self.user_choice == 'paper':
                print(' Congratulations, you won ')
            elif self.user_choice == 'rock':
                print("It's a draw, go again")
            else:
                print( 'You lost')
        
        if self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                print(' Congratulations, you won')
            elif self.user_choice == 'paper':
                print("it's a draw, go again ")
            else:
                print(' You lost')
        
        if self.computer_choice == 'scissors':
            if self.user_choice == 'rock':
                print(' Congratulations, you won') # I dont really know much about the games's rules, i just used my initiative
            elif self.user_choice == 'scissors':
                print(" it's a draw")
            else:
                print('You lost the game')


def play_game(self, get_winner):
    play_game = RockPaper()
    self.computer_choice(get_winner)
    self.user_choice(get_winner)
    self.get_winner()
    #class # how to instantiate the class, define computer choice and user choice. call the get winner function

            
if __name__ == '__main__':
    play_game
    


            



    