import logging
from .constants import NUMBERS, UNITS


def __low_number_to_english(number):
    """Translate the numbers below 100
    """
    if number <= 20:
        text_number = NUMBERS[number]
    else:
        rest = number % 10
        initial = number - rest
        text_number = f"{NUMBERS[initial]} {NUMBERS[rest]}"
    return text_number


def number_to_english(number):
    """ "Translates" an integer number to plain english

    Args:
        number (int): the number to "translate"

    Return:
        The string version of number
    """
    text_number = ""

    if number < 100:
        return __low_number_to_english(number)

    for unit, text_unit in UNITS.items():
        # print(text_unit)
        initial = number // unit
        number = number % unit
        # print(initial, number)

        if text_number and not initial:
            break

        if initial != 0:
            text_number += number_to_english(initial) + " " + text_unit + " "
        if number > 0 and number < 100:
            text_number += number_to_english(number)

    return text_number
