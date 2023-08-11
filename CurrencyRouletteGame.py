import random
from currency_converter import CurrencyConverter
from Live import check_input_int


def get_money_info():
    random_usd = random.randrange(1, 100)
    return random_usd, int(CurrencyConverter().convert(random_usd, "USD", "ILS"))


def get_guess_from_user():
    return check_input_int()


def currency_roulette_game_play(difficulty):
    value_in_usd, value_in_ils = get_money_info()
    print(f"How much {value_in_usd} dollars are worth in shekels?")
    return (value_in_ils - (5 - difficulty)) <= get_guess_from_user() <= (value_in_ils + (5 - difficulty))
