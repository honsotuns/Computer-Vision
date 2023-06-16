
import random

class RPS:
    ''' init method with choices_list as its parameter '''
    def __init__(self, choices_list):
        self.choices_list = choices_list

    ''' This method gets player's choice using an input function '''
    def get_user_choice(self):
        user_choice = input("Kindly enter your choice: ").lower()
        if user_choice not in choices_list:
             print("Please enter a valid choice")

        elif user_choice in choices_list:
             print("Computer will make its choice")
        return user_choice
    
    ''' This method gets computer's choice, using random function '''
    def get_computer_choice(self):
        computer_choice = random.choice(choices_list)
        return computer_choice
    
    ''' This method computes the game's logic using if statement to determine the winner '''
    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print(f" Its a draw, lets go again! The computer chose {computer_choice}. Same as you!")

        elif user_choice == "rock" and computer_choice == "paper":
            print(f"You lost! The computer picked {computer_choice}") 
        
        elif user_choice == "paper" and computer_choice == "scissors":
            print(f" You lost! The computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "rock":
            print(f" You lost! The computer picked {computer_choice}") 

        elif user_choice == "rock" and computer_choice == "scissors":
            print(f" You won! The computer picked {computer_choice}") 
        
        elif user_choice == "paper" and computer_choice == "rock":
            print(f" You won! The computer picked {computer_choice}")         

        elif user_choice == "scissors" and computer_choice == "paper":
            print(f" You won! the computer picked {computer_choice}")

''' The play_game method '''            
def play_game(choices_list):
    game = RPS(choices_list)
    user_choice = game.get_user_choice()
    computer_choice = game.get_computer_choice()
    game.get_winner(user_choice, computer_choice)

if __name__ == '__main__': 
    choices_list = ['rock', 'paper', 'scissors']
    play_game(choices_list)