# Computer-vision
A Python program that plays the classic game of Rock, Paper, Scissors

Milestone 1:
* Setting up the environment
* Github set up

Milestone 2:
* Creating a computer vision model that detects whether the player is showing Rock, Paper or Scissors to the camera
* Creating an image project model with 4 different classes : Rock, Paper, scissors, Nothing
* Downloading the model from "Tensorflow" tab in Teachable-Machine. The model was named keras_model.h5 and the text file containing the labels was named labels.txt.

Milestone 3:
* Installation of all dependencies
* Creating a new virtual environment
* "my_env" is the name of the environment created.

Milestone 4: Creating a Rock-Paper_ Scissors game
* This code randomly choose an option (rock, paper, or scissors) and then ask the user for an input.
* Another file called manual_rps.py was created, that will be used to play the game without the camera.
* Program used the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.
* Using "if-elif-else" statements, the script chooses a winner based on the classic rules of Rock-Paper-Scissors.
* If the computer wins, the function prints "You lost", if the user wins, the function prints "You won!", and if it's a tie, the function prints "It is a tie!".

Milestone 5:
Using the camera to play Rock-Paper-Scissors game
* The hard-coded user guess is replaced with the output of the computer vision model. A new file is created called camera_rps.py where the codes were written
* Game is repeated until a player gets 3 wins
