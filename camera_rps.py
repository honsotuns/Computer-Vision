import cv2
from keras.models import load_model
import numpy as np
import random
import time


class RPS:
    
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.computer_wins = 0
        self.user_wins = 0
    
    def count_countdown(self):
        countdown = 5
        print(" Please prepare to show your choice ")
        while countdown > 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print(' Please show your hand now')     

    def get_prediction(self):
        end = time.time() + 1
        while time.time() < end:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            self.data[0] = normalized_image
            cv2.imshow('frame', frame)
            prediction = self.model.predict(self.data)
            print(prediction)
            self.choice = choices_list[prediction.argmax()]
            print(f"You chose {self.choice}")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.choice        

    def get_computer_choice(self):
        computer_choice = random.choice(choices_list)
        return computer_choice

    def get_winner(self, choice, computer_choice):
        if self.choice == "nothing":
            print("Restart, you've not made a choice! ")

        elif choice == computer_choice:
            print(f" Oh Its a draw! The computer chose {computer_choice}. Same as you! ")

        elif (choice == "rock" and computer_choice == "paper") or \
            (choice == "paper" and computer_choice == "scissors") or \
            (choice == "scissors" and computer_choice == "rock"):
                print(f" You lost! The computer picked {computer_choice}")
                self.computer_wins += 1

        else:
            self.user_wins += 1

        
def play_game(choices_list):
    game = RPS()
    while True:
        game.count_countdown()
        user_choice = game.get_prediction()
        computer_choice = game.get_computer_choice()
        game.get_winner(user_choice, computer_choice)
        print(f"Computer wins: {game.computer_wins} ---- User wins: {game.user_wins}")

        if game.user_wins == 3 or game.computer_wins == 3:
            print(f"The game is over, Computer won {game.computer_wins} and you won {game.user_wins}")
            break


    game.cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    choices_list = ['rock', 'paper', 'scissors', 'nothing']
    play_game(choices_list)
    