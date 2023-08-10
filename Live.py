def welcome(name):
    welcome_format = f"""
    \rHello {name} and welcome to the World of Games (WoG).
    \rHere you can find many cool games to play.
    """
    print(f"{welcome_format}")


def check_valid_choice(min_value, max_value, input_value):
    if min_value <= input_value <= max_value:
        return True

    print(f"Invalid input. Please choose a number between {min_value} to {max_value}")
    return False


def check_input_int():
    int_input = -1

    str_input = input()
    if str_input.isdigit():
        int_input = int(str_input)

    return int_input


def checks(min_value, max_value):
    user_choice = check_input_int()
    while not check_valid_choice(min_value, max_value, user_choice):
        user_choice = check_input_int()
    return user_choice


def choosing_menu():
    confirmation = " "
    game_chosen = 0
    game_difficulty = 0

    game_list = ["Memory Game", "Guess Game", "Currency Roulette"]
    game_list_format = """Please choose a game to play:
        \r\t1. Memory Game - a sequence of numbers will appear for 0.7 second and you have to guess it back in order
        \r\t2. Guess Game - guess a number and see if you chose like the computer
        \r\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""
    game_difficulty_format = "Please choose game difficulty from 1 to 5: "

    print(f"{game_list_format}")
    game_chosen = checks(1, 3)

    print(game_difficulty_format)
    game_difficulty = checks(1, 5)

    return game_list[game_chosen - 1], game_difficulty


def confirm_choice():
    confirmation = str(input())
    while not confirmation.lower() == "y" and not confirmation.lower() == "n":
        print("Invalid answer, Please enter y to confirm or n to return to menu")
        confirmation = str(input())

    return confirmation.lower() == "y"


def confirm_game_choice():
    player_choice = choosing_menu()

    while True:
        game_confirm_form = (f"You have chosen to play {player_choice[0]} with difficulty {player_choice[1]}.\r\n" +
                             "Are you sure about your choice? y/n")
        print(f"{game_confirm_form}")
        if confirm_choice():
            return player_choice[0], player_choice[1]
        else:
            choosing_menu()


def load_game():
    return confirm_game_choice()
