import time


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
    Question("What was sonic the hedgehogs original name?", "Mr.Needlemouse", "d", ["(a) Mr.Pricklepants", "(b) Shadow the hedgehog", "(c) Danger Mouse", "(d) Mr.Needlemouse"])
]


def gamer_quiz_logo():
    """
    Creates an ascii gamer quiz logo at program start
    """
    logo = ["logo1.txt", "logo2.txt", "logo3.txt", "logo4.txt", "logo5.txt", "logo6.txt"]
    frames = []
    for file in logo:
        f = open(file,"r", encoding="utf8")
        frames.append(f.readlines())
        f.close()
    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)


def ask_question():
    """
    Ask the user a question from the questions list, present four possible answers,
    and check it against the correct answer (Or its corresponding letter)
    """
    score = 0
    question_counter = 0
    lives = 3
    for question in questions:
        question_counter += 1
        print(f"Question {question_counter}")
        print(question.question_text)
        for option in question.answer_options:
            print(option)

        answer = ""
        while not answer:
            answer = input("-->").strip().lower()
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
            print(f"You said {answer}, Thats right!")
            score += 1
        elif answer in question.other_answer:
            print(f"You said ({answer}) {question.correct_answer}, Thats right!")
            score += 1
        else:
            print(f"{answer} is incorrect, the correct answer is ({question.other_answer}){question.correct_answer}")
            lives -= 1
            if lives == 0:
                print("Hard Luck, you ran out of lives!")
                break
    print(f"you got {score} out of {question_counter} questions correct!")


def get_user_data():
    """
    Print welcome message and get username
    """
    print("\nWelcome to the Gamer Quiz!\n")
    time.sleep(0.5)
    username = input("Please enter your username --> ")
    return username


def main():
    """
    Run all gamer-quiz functions
    """
    gamer_quiz_logo()
    username = get_user_data()
    ask_question()


main()
