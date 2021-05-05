from unittest import TestCase

from .calculator import calculator, Calculator, PetFriend


class CalculatorTest(TestCase):
    def test_calculator_works(self):
        result = calculator(numbers=5, price=5000, original_delivery_fee=0)

        # ((price * numbers) - discount + delivery) / numbers
        self.assertEqual(result, 4000)

    def test_calculator_class(self):
        c = Calculator(number=5, price=5000, original_delivery_fee=0, discount=5000, addtional_discount=0)

        self.assertEqual(c.price_per_unit, 4000)

    def test_petfriends(self):
        pf = PetFriend(number=5, price=5000)

        self.assertEqual(pf.price_per_unit, 4000)
