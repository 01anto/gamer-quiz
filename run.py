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


main()
