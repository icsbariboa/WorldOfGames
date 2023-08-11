import random
from currency_converter import CurrencyConverter
from Live import check_input_int

CONVERTOR = CurrencyConverter()


def get_money_info():
    random_usd = random.randrange(1, 100)
    value_in_ils = int(CONVERTOR.convert(random_usd, "USD", "ILS"))
    return random_usd, value_in_ils


def get_guess_from_user():
    return check_input_int()


def currency_roulette_game_play(difficulty):
    value_in_usd, value_in_ils = get_money_info()
    min_answer, max_answer = (value_in_ils - (5 - difficulty)), (value_in_ils + (5 - difficulty))
    print(f"How much {value_in_usd} dollars are worth in shekels?")
    user_guess = get_guess_from_user()
    return min_answer <= user_guess <= max_answer
