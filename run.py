import sys
import time
import os
os.system("clear")


class Question:
    """
    Creates an instance of Question
    """
    def __init__(self, question_text, correct_answer, other_answer, answer_options):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.other_answer = other_answer
        self.answer_options = answer_options


questions = [
    Question("What company produces mario games?", "nintendo", "c", ["(a) Sony", "(b) Sega", "(c) Nintendo", "(d) Microsoft"]),
    Question("In what game will you find a creeper?", "minecraft", "a", ["(a) Minecraft", "(b) Terraria", "(c) Roblox", "(d) Fortnite"]),
    Question("On what game console did crash bandicoot first appear?", "playstation", "c", ["(a) Dreamcast", "(b) Gamecube", "(c) Playstation", "(d) Xbox"]),
    Question("Which cancelled game was Hideo Kojima working on before he left konami?", "silent hill", "b", ["(a) Resident Evil", "(b) Silent Hill", "(c) Dying light", "(d) The Thing"]),
    Question("What was sonic the hedgehogs original name?", "Mr.Needlemouse", "d", ["(a) Mr.Pricklepants", "(b) Shadow the hedgehog", "(c) Danger Mouse", "(d) Mr.Needlemouse"]),
    Question("Who is the main antagonist in final fantasy 7?", "Sephiroth", "b", ["(a) Chocobo", "(b) Sephiroth", "(c) Yu Yevon", "(d) Dhoulmagus"]),
    Question("In Metal gear solid 1, which song was sung in Irish?", "The Best Is Yet To Come", "a", ["(a) The Best Is Yet To Come", "(b) Snake Eater", "(c) Nuclear", "(d) Poor Misguided Fool"]),
    Question("Who is the main character in Devil May Cry?", "Dante", "d", ["(a) Mundus", "(b) Vergil", "(c) Griffon", "(d) Dante"]),
    Question("What was the first Mega Man game on the Super Nintendo (SNES)?", "Mega Man X", "b", ["(a) Mega Man", "(b) Mega Man X", "(c) Mega Man X 2", "(d) Mega Man X 3"]),
    Question("What is the main weapon used in Kingdom Hearts?", "Keyblade", "c", ["(a) Chakram", "(b) Excaliber", "(c) Keyblade", "(d) Lightsaber"])
]


def gamer_quiz_logo():
    """
    Creates an ascii gamer quiz logo at program start
    """
    logo = ["logo1.txt", "logo2.txt", "logo3.txt", "logo4.txt", "logo5.txt", "logo6.txt"]
    frames = []
    for file in logo:
        f = open(file, "r", encoding="utf8")
        frames.append(f.readlines())
        f.close()
    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)


def get_user_data():
    """
    Print welcome message and get username
    """
    print("\nWelcome to the Gamer Quiz!\n")
    time.sleep(0.5)
    username = input("Please enter your username --> ")
    return username


def ask_question(username):
    """
    Ask the user a question from the questions list. Present four possible
    answers. Take input, perform validation and compare input to correct_answer
    or other_answer. Adjust score, and question_counter accordingly.
    Allow the user to quit in game by giving 'q' as answer.
    """
    score = 0
    question_counter = 0
    print(f"\nHey {username}, Here comes your questions!\n")
    for question in questions:
        question_counter += 1
        print(f"Question {question_counter}")
        print(f"{question.question_text}")
        for option in question.answer_options:
            print(option)
        answer = ""
        while not answer:
            answer = input(f"-->\n").strip().lower()
            if answer == "q":
                sys.exit(f"You have chosen to quit, Farewell {username}!")
            if answer == "":
                print("You didn't enter anything - please enter some text!")
                continue
            if len(answer) >= 2:
                continue
            answer_set = ['a', 'b', 'c', 'd']
            if answer not in answer_set:
                print("You didn't give an actual option - enter a, b, c or d or type out your answer")
                answer = ""
                continue
        if answer == question.correct_answer.lower():
            print(f"You said {answer}, Thats right!\n")
            score += 1
        elif answer in question.other_answer.lower():
            print(f"You said ({answer}) {question.correct_answer}, Thats right!\n")
            score += 1
        else:
            print(f"{answer} is incorrect, the correct answer is ({question.other_answer}) {question.correct_answer}\n")
    return username, score, question_counter


def progress_report(username, score, question_counter):
    """
    Informs the user at the end of the game what score they got,
    prints a different message depending on that score and calls
    the repeat_or_leave function
    """
    print(f"you got {score} out of {question_counter} questions correct!")
    if score == 0:
        print(f"You got none of these at all {username}? I must be getting old! :)")
    elif score <= 9:
        print(f"Your pretty good {username}! :)")
    elif score == 10:
        print(f"{username}, you show off! You got everything right, Well Done! :)")
    repeat_or_leave(username)


def repeat_or_leave(username):
    """
    Provides the user with an option to play the game again or quit.
    """
    response = ""
    while not response:
        print("Would you like to go again? (y or n)")
        response = input(f"-->\n").strip().lower()
        if response == "y":
            print("Okay here we go again!")
            main()
        if response == "n":
            sys.exit(f"Okay Farewell {username}!")
        else:
            print("Please Enter y or n")
            response = ""
            continue


def main():
    """
    Run all gamer-quiz functions
    """
    gamer_quiz_logo()
    username = get_user_data()
    username, score, question_counter = ask_question(username)
    progress_report(username, score, question_counter)


main()
