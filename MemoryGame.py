import random
import time
from Live import checks

COUNT = 3


def generate_sequence(difficulty):
    return random.choices(range(1, 101), k=difficulty)


def get_list_from_user(difficulty):
    print("\rPlease enter the numbers you remember:", end="")
    return [checks(1, 101) for i in range(difficulty)]


def is_list_equal(user_list, random_list):
    return user_list == random_list


def memory_game_play(difficulty):
    random_list = generate_sequence(difficulty)
    print("the list will be shown in:")

    for number in range(COUNT):
        print(f"\r{COUNT - number}", end="")
        time.sleep(1)

    print(f"\r{random_list}", end="")
    time.sleep(0.7)

    return is_list_equal(random_list, get_list_from_user(difficulty))
