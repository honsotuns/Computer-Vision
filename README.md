# Computer-vision
Computer Vision Rock-Paper-Scissors (RPS) project, which trained a computer vision model using Teachable-Machine. The model detects whether the user shows Rock, Paper, or Scissors to the camera, so the user can leverage that output to play an RPS game with the computer.
* Trained a computer vision model that detected gestures in real-time.
* Created a Python script to apply the programming logic using the Tensorflow API and OpenCV


 1:
* Setting up the environment
* Github set up

2:

* Creating an image project model with four different classes: Rock, Paper, Scissors, Nothing
* Dowmload the model
   * Downloaded the model from the "Tensorflow" tab in Teachable-Machine. The model is named keras_model.h5 and the text file containing the labels is named labels.txt


 3:
* Installation of all dependencies
* Creating a new virtual environment
* Created a conda environment and then install the necessary requirements. Used opencv-python, tensorflow, and ipykernel
* "my_env" is the name of the environment created.
* requirements.txt created

 4: Creating a Rock-Paper-Scissors game
* This code randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
* Created two methods: get_computer_choice and get_user_choice
* The first method will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
* The second method will ask the user for an input and return it
* Created a method to simulate the game (get_computer_choice, get_user_choice, and get_winner)
* Another file called manual_rps.py was created, that will be used to play the game without the camera
* Program used the random module to pick a random option between rock, paper, and scissors for computer's choice and the input function to get the user's choice
* Using "if-elif-else" statements, the script chooses a winner based on the classic rules of Rock-Paper-Scissors
* If the computer wins, the function prints "You lost", if the user wins, the function prints "You won!", and if it's a tie, the function prints "It is a tie!"

 5:
Using the camera to play Rock-Paper-Scissors game
* The hard-coded user guess is replaced with the output of the computer vision model. A new file is created called camera_rps.py where the codes were written
* Game is repeated until either a player gets 3 wins or the computer gets 3 wins

 
   * To run: python camera_rps.py 
