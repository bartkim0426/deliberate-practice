from unittest import TestCase
from unittest.mock import patch, call

import tip_calculator


def prompt_test():
    a = input('1')
    b = input('2')
    return a, b

def print_test():
    print('hello')
    print('world')

class CalculatorTestCase(TestCase):
    @patch('tests.input', create=True)
    def test_mock_input(self, mock_input):
        '''
        test for how to mock prompt input in python
        '''
        mock_input.side_effect = ['1', '2']

        result = prompt_test()
        self.assertEqual(result, ('1', '2'))

    @patch('builtins.print')
    def test_mock_print(self, mock_print):
        '''test for how to mock print in python'''
        print_test()
        mock_print.assert_has_calls([call('hello'), call('world')])

    @patch('builtins.print')
    @patch('tip_calculator.input', create=True)
    def test_calculator(self, mock_input, mock_print):
        '''
        input:
            bill: 11.25
            tip rate: 15
        output:
            tip: $1.69
            total: $12.94
        '''
        mock_input.side_effect = ['11.25', '15']
        result = tip_calculator.calculate_tip()

        calls = [call('Tip: $1.69'), call('Total: $12.94')]
        mock_print.assert_has_calls(calls)
        self.assertEqual(result, (1.69, 12.94))

    @patch('tip_calculator.input', create=True)
    def test_enter_input(self, mock_input):
        mock_input.side_effect = ['11.25', '15']
        calculator = tip_calculator.TipCalculator()

        # enter input from prompt
        calculator._enter_input()

        self.assertEqual(calculator.bill, '11.25')
        self.assertEqual(calculator.tip_rate, '15')

    @patch('tip_calculator.input', create=True)
    def test_enter_input_with_invalid(self, mock_input):
        mock_input.side_effect = ['invalid', '11.25', '15']
        calculator = tip_calculator.TipCalculator()

        # enter input from prompt
        calculator._enter_input()

        self.assertEqual(calculator.bill, '11.25')
        self.assertEqual(calculator.tip_rate, '15')

    def test_is_float(self):
        calculator = tip_calculator.TipCalculator()

        self.assertFalse(calculator._is_float('not_float'))
        self.assertTrue(calculator._is_float('1.11'))

    def test_is_validate_for_valid_value(self):
        calculator = tip_calculator.TipCalculator()

        calculator.bill = '1.1'
        calculator.tip_rate = '15'

        calculator._validate()

    def test_is_validate_for_invalid_value(self):
        calculator = tip_calculator.TipCalculator()

        calculator.bill = 'not_valid'
        calculator.tip_rate = '15'

        with self.assertRaises(ValueError):
            calculator._validate()

    def test_calculate_tip(self):
        calculator = tip_calculator.TipCalculator()
        calculator.bill = '11.25'
        calculator.tip_rate = '15'

        calculator._calculate_tip()

        self.assertEqual(calculator.tip, 1.69)
        self.assertEqual(calculator.total, 12.94)

    @patch('builtins.print')
    def test_print_output(self, mock_print):
        calculator = tip_calculator.TipCalculator()
        calculator.bill = '11.25'
        calculator.tip_rate = '15'

        calculator._calculate_tip()
        calculator._print_output()

        calls = [call('Tip: $1.69'), call('Total: $12.94')]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    @patch('tip_calculator.input')
    def test_proceed(self, mock_input, mock_print):
        '''test proceed whole input -> output process'''
        mock_input.side_effect = ['11.25', '15']
        calculator = tip_calculator.TipCalculator()
        # proceed input to output
        calculator.proceed()

        calls = [call('Tip: $1.69'), call('Total: $12.94')]
        mock_print.assert_has_calls(calls)
