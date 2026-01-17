import random
import tkinter as gui

""" 
In the game the user will be required to answer 
a number of questions based on the difficulty selected.
The total score will be presented at the end as well as
the highest score if they have played before
"""

# PAGE DESIGN
home_page = gui.Tk()
home_page.geometry("500x500")
home_page.title(str("The Calculation Game"))
home_page.configure(background="#F54927")



# GLOBAL VARIABLES 
player_name = ""
name_entry = None

points = 0
qnumber = 0
qmax = 0

high_score = {} 
user_answer = 0
difficulty = ""

#GAME CODE

def welcome_page():
    """
    The user is required to input their name to progress
    """
    for d in home_page.winfo_children():
        d.destroy() 

    gui.Label(home_page, text="Welcome to The Calculation Games!!!").pack()

    global name_input
    name_input = gui.Entry(home_page)
    name_input.pack()

    gui.Label(home_page, text="Firstly, What is your name?").pack()

 

    gui.Button(home_page, text="PROCEED", command=difficulty_selection).pack()
#ALL NAMES CHANGED JUST NEED TO CHECK WHAT ELSE CAN BE CHANGED 

def difficulty_selection():
    """
   The user name is saved and the user selects their difficulty level. Maths Wiz or Standard
    """
    global player_name 
    player_name = name_input.get().strip()
    if not player_name:
        gui.Label(home_page, text="Please enter a name").pack()
        return

    for d in home_page.winfo_children(): 
        d.destroy()

    gui.Label(home_page, text="Welcome " + player_name + ", I hope you are up for the challenge").pack()
    gui.Label(home_page, text="Please select your difficulty - Standard or Maths Wizard if you dare!").pack()

    gui.Button(home_page, text="Standard", command=lambda: start_game("Standard")).pack()
    gui.Button(home_page, text="Maths Wiz", command=lambda: start_game("Maths Wizard")).pack()


def start_game(level): 
    """
    The difficulty that is selected determines the num of questions and the highest possible value in the calculation
    """
    global difficulty, points, qnumber, qmax, max_value
    difficulty = level
    points = 0
    qnumber = 0

    if level == "Maths Wizard":
        max_value = 10
        qmax = 15
    else:
        level == "Standard"
        max_value = 5
        qmax = 10

    qnext()


def qnext():
    """
    Display the next question or end the quiz if all questions are done.
    Generates a random addition or multiplication question.
    """
    global qnumber, user_ans
    if qnumber >= qmax:
        end_of_game()
        return

    for d in home_page.winfo_children():
        d.destroy()

    qnumber += 1

    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    operation = random.choice(["+", "*"])

    if operation == "+": #ADDITION CALULATIONS
        user_ans = num1 + num2
        equation = str(num1) + "+" + str(num2) +" = ?"
        
    else:                                  
        user_ans= num1 * num2 #MULTIPLICATION CALULATIONS
        equation = str(num1) + "x" + str(num2) +" = ?"

    gui.Label(home_page, text= "Question " + str(qnumber) + " of " + str(qmax)).pack()
    gui.Label(home_page, text=equation).pack()

    response_label = gui.Label(home_page, text="")
    response_label.pack()

    user_answer = gui.Entry(home_page)
    user_answer.pack()

    gui.Button(home_page, text="Let's check", command=lambda: answer_val(user_answer, response_label)).pack()


def answer_val(entry, response_label): #used to validate all answers
    """
    The user's answer is valuidated and the score is updated if required. 
    Null submissions are not allowed.
    """
    global points
    user_input = entry.get().strip()
    if not user_input:
        response_label.config(text="Please type an answer!")
        return

    if user_input.isdigit() and int(user_input) == user_ans:
        points += 1
        response_label.config(text="Well done! Next Question")

    else:
        response_label.config(text=f"Nice Try! The answer is {user_ans}")

    home_page.after(2000, qnext)


def end_of_game():
    """
   The user's name and score is displayed, as well as the highest score
   The user gets the opportunity to play again 
    """
    global high_score
    for d in home_page.winfo_children():
        d.destroy()

    if player_name not in high_score or points > high_score[player_name]: 
        high_score[player_name] = points

    gui.Label(home_page, text="Challenge Finished!").pack()
    gui.Label(home_page, text=f"{player_name}, You scored: {points}/{qmax}").pack()
    gui.Label(home_page, text=f" And your highest score: {high_score[player_name]}").pack()

    gui.Button(home_page, text="Do you want to play again?", command=welcome_page).pack()

welcome_page()
home_page.mainloop()