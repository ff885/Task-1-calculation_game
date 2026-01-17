#THE CALCULATION GAME

DESCRIPTION
The Calculation Game is a simple question and answer quix designed to test basic arithmetic skills. The player starts nby inputting their name and selecting a difficulty which determines the type of question they will be required to answer. These questions are random and answers are given as soon as the user locks in their answer. The score is tracked and presented at the end as well as the highscore. The user is then given the opportunity to try again.

GAME REQUIREMENTS
- Python installed on your device (See FAQs)
- Tkinter Library (This tends to inbuilt with python)
- An IDE to run the game

Download the script and run the script through your local terminal
E.g python the_calculation_game.py
  
GAME INSTRUCTIONS
1. Once the terminal is opened and the screen appears, enter your name as prompted
   You cannot proceed unless your name is entered
2. The user must choose a difficulty:
   STANDARD - The easiest version
   MATHS WIZARD - A harder version that requires the user to answer more questions
4. Everytime a quesytion appears, submit the answer you think is correct
5. Click the button below to submit the answer
6. A response will be generated staright away, notifying the user if it is correct or incorrect
7. The user is also given the right anwer if the answer is incorrect
8. At the end of the game, the total score and the personal high score will be displayed
9. The user is given the option to play again or they can close the window

TECHNICAL DOCUMENTATION
The game is clealry set out in stages as shown by the functions: 

welcome_page() – Welcomes the user to the game and they can input their name
difficulty_selection() – The user selects a level which determines the operations used in the questions and the number of questions
start_game() – The scores are set to zero and the questions are set
qnext() – A new question is randomly generated until the qmax is reached 
answer_val() – The inputted answers are checked and the points are updayed accordingly.
end_of_game() – The user's total points and highscore are displayed and they get the opportunity to play again

Key Variables
player_name - It saves the name the user inputs at the beginning
points - Tracks every question the user gets correct and updates the total score
qnumber	- Tracks how many questions have been answered until it reached the maximum (qmax)
qmax - Indicates the maximum amount of questions for each difficulty level 
user_ans -	Stores the user input and checks if it is correct
high_score - Saves the total score after each game within a single session to compare to the previous score
difficulty - Checks which level the user selected 

QUESTION DESIGN
random.randint() - Random number are generated for each question
random.choice() - An operation is chosen for each level

GUI
This program utelises Tkinter for the user interface. The general text (instrucution and questions) are shown by Labels and Entry is used so the user can input their name and the answer to the questions
I designed the window to be 500 x 500 which is a fair size and a light pink colour to welcome the user


FUTURE CONSIDERATION
I want to add a timer to increase to the difficulty. 
Currrently there are only two difficulty levels so I will add a medium level and further increase the distinction by using one operation for STANDARD, two for MEDIUM and three for MATHS WIZ.
I want to also look into saving the highscores for multiple users and to make it permanent as the currenty program doesn't save the score once the program is closed.
In future iterations, I may also look at adding features that allow the user to change the background colour themselves.

FAQs
What if I have difficulty installing python?
Please follow this link -> https://www.python.org/downloads/

Furthermore if there are any other question, feel free to reach out at thecalgames@gmail.com and we will answer within 24 hours. We also welcome any feedback

