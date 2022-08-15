
import random

class RockPaper:

    def __init__(self, get_computer_choice, get_user_choice, get_winner, game ):
       self.get_computer_choice = get_computer_choice 
       self.get_user_choice = get_user_choice
       set.get_winner = get_winner
       self.game = game


    def get_computer_choice(self, computer_choice):
        self.computer_choice = random.choice(computer_choice)
        self.get_user_choice()
    

    def get_user_choice(self, user_choice):
        self.get_user_choice = input (" Please choose Rock, Paper, or Scissors ").lower()
        if self.user_choice not in self.game:
            print (" Kindly choose among the options")
        else:
            self.get_winner()
    
def get_winner(self, get_winner):

        print(f" You've chosen {self.get_user_choice}. The computer chose {self.computer_choice} ")
        
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
    
    #def play(self, play, game):
       # self.play(game)

                
if __name__ == '__main__':
    game_list = [' rock', 'paper', 'scissors' ]
    get_winner(game_list)
    
    


            



    