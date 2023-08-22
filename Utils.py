import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def screen_clear():
    os.system("cls" if os.name == "nt" else "clear")
