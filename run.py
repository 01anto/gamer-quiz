import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gamer_quiz')


class Question:
    def __init__(self, questionText, correctAnswer, answerOptions=None):
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.answerOptions = answerOptions


questions = [
    Question("What company produces mario games", "nintendo",["(a) Sony", "(b) Sega", "(c) Nintendo", "(d) Microsoft"]),
    Question("In what game will you find a creeper", "minecraft",["(a) Minecraft", "(b) Terraria", "(c) Roblox", "(d) Fortnite"]),
    Question("On what game console did crash bandicoot first appear", "playstation",["(a) Dreamcast", "(b) Gamecube", "(c) Playstation", "(d) Xbox"]),
    Question("Which of the following games did Hideo Kojima work on", "silent hill",["(a) Resident Evil", "(b) Silent Hill", "(c) Dying light", "(d) The Thing"]) 
]


def ask_question():
    """
    Ask the user a question from the questions list and check it against the correct answer
    """
    for question in questions:
        if (question.answerOptions != None):
            print(question.questionText)
            for option in question.answerOptions:
                print(option)
            answer = input(f"-->")
        else:
            print(question.questionText)
            answer = input(f"-->")

        if answer.lower() == question.correctAnswer.lower():
            print(f"You said {answer}, Thats right!")
        else:
            print(f"{answer} is incorrect, the correct answer is {question.correctAnswer}")


def get_user_data():
    """
    Get user data and password input from the user
    """
    username = input("Please enter your username --> ")
    password = input("Please enter your password --> ")
    return username, password


def update_user_details_worksheet(data):
    """
    Update user_details worksheet, Add a new row for username and password
    """
    print("Updating user_details worksheet")
    user_details_worksheet = SHEET.worksheet("user_details")
    user_details_worksheet.append_row(data)
    print("user_details worksheet updated successfully.\n")


def main():
    """
    Run all gamer-quiz functions
    """
    data = get_user_data()
    update_user_details_worksheet(data)
    ask_question()


main()
