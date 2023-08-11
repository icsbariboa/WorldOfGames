from Live import load_game, welcome, confirm_choice
from GuessGame import guess_game_play
from MemoryGame import memory_game_play
from CurrencyRouletteGame import currency_roulette_game_play


def game():
    while True:
        game_name, game_difficulty = load_game()

        if game_name.lower() == "memory game":
            print("win" if memory_game_play(game_difficulty) else "lose")
        if game_name.lower() == "guess game":
            print("win" if guess_game_play(game_difficulty) else "lose")
        if game_name.lower() == "currency roulette":
            print("win" if currency_roulette_game_play(game_difficulty) else "lose")
        print("Do you want to play another game? y/n")
        if not confirm_choice():
            break


def main():
    welcome(input("Please enter your name: "))
    game()


if __name__ == "__main__":
    main()
