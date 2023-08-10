import random
from Live import checks


def generate_number(difficulty):
    return random.randrange(1, difficulty + 1)


def get_guess_from_user(difficulty):
    print(f"Please enter a number between 1 to {difficulty + 1}")
    return checks(1, difficulty + 1)


def compare_results(secret_number, guessed_number):
    return secret_number == guessed_number


def guess_game_play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))
