from Live import load_game, welcome, confirm_choice
from GuessGame import guess_game_play
from MemoryGame import memory_game_play
from CurrencyRouletteGame import currency_roulette_game_play
from Score import add_score
from Utils import screen_clear


def game():
    while True:
        game_name, game_difficulty = load_game()

        if game_name.lower() == "memory game":
            if memory_game_play(game_difficulty):
                add_score(game_difficulty)
                print("win")
            else:
                print("lose")
        if game_name.lower() == "guess game":
            if guess_game_play(game_difficulty):
                add_score(game_difficulty)
                print("win")
            else:
                print("lose")
        if game_name.lower() == "currency roulette":
            if currency_roulette_game_play(game_difficulty):
                add_score(game_difficulty)
                print("win")
            else:
                print("lose")
        print("Do you want to play another game? y/n")
        if not confirm_choice():
            screen_clear()
            break


def main():
    welcome(input("Please enter your name: "))
    game()


if __name__ == "__main__":
    main()
