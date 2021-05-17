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
