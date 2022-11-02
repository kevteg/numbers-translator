from django.test import TestCase
from apps.translator.utils.translate import number_to_english


class TestNumberToEnglish(TestCase):

    numbers = [
        (10, "ten"),
        (35, "thirty five"),
        (101, "one hundred one"),
        (1005, "one thousand five"),
        (10009, "ten thousand nine"),
        (102289, "one hundred two thousand two hundred eighty nine"),
        (
            12345678,
            "twelve million three hundred forty five thousand six hundred seventy eight",
        ),
        (
            1200112223,
            "one billion two hundred  million one hundred twelve thousand two hundred twenty three",
        ),
    ]

    def test_number_output(self):
        for number, number_text in self.numbers:
            processed_number_text = number_to_english(number)
            # equivalent to pytest parameterize
            with self.subTest("Testing number", number=number):
                self.assertEqual(processed_number_text, number_text)
