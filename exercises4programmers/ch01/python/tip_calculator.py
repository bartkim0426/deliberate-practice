from dataclasses import dataclass


def calculate_tip() -> tuple:
    '''
    enter bill and tip_rate from prompt, print tip and total amount
    '''
    bill: str = input('What is the bill amount?')
    tip_rate: str = input('What is the tip rate?')

    bill, tip_rate = float(bill), float(tip_rate)

    tip = bill * (tip_rate / 100)

    tip = round(tip, ndigits=2)

    total = tip + bill

    print("Tip: $" + str(tip))
    print("Total: $" + str(total))
    
    return tip, total


@dataclass
class TipDataClass:
    bill: float
    tip_rate: int
    tip: float
    total: float

    def __init__(self, bill, tip_rate):
        self.bill = bill
        self.tip_rate = tip_rate
        self._calculate_tip(bill, tip_rate)

    def _calculate_tip(self, bill: float, tip_rate: int):
        '''set tip and total after calculate with bill and tip_rate'''
        self.tip = round(bill * (tip_rate / 100), ndigits=2)
        self.total = self.bill + self.tip


class TipCalculator:
    '''
    Tip calculator from bill and tip_rate

    arguments:
        bill: float
        tip_rate: int

    interfaces:
        _validate
        calculate_tip
        enter_input
        print_output
    '''
    def __init__(self):
        pass
        # self._enter_input()

    def _enter_input(self):
        '''
        enter input for bill and tip_rate from prompt

        Continuously receive input if the input value is invalid
        '''
        self.bill: str = input('What is the bill amount? ')
        while not self._is_float(self.bill):
            print('Wrong bill. Bill should be number or float only.')
            self.bill: str = input('What is the bill amount? ')

        self.tip_rate: str = input('What is the tip rate? ')
        while not self.tip_rate.isdigit():
            print('Wrong tip_rate. Tip_rate should be number')
            self.tip_rate: str = input('What is the tip rate? ')

    def _print_output(self):
        '''print output of tip and total bill'''
        print(f'Tip: ${self.tip}')
        print(f'Total: ${self.total}')

    def _is_float(self, x: str) -> bool:
        '''check if input x is float or not'''
        try:
            float(x)
        except ValueError:
            return False
        return True

    def _validate(self):
        try:
            assert self._is_float(self.bill)
            assert self.tip_rate.isdigit()
        except AssertionError as e:
            raise ValueError(f'Invalid Value: {e}')

    def _calculate_tip(self):
        bill = float(self.bill)
        tip_rate = int(self.tip_rate)
        tip_data = TipDataClass(bill=bill, tip_rate=tip_rate)

        self.tip = tip_data.tip
        self.total = tip_data.total

    def proceed(self):
        '''proceed calculator by getting input from prompt and output to prompt'''
        self._enter_input()
        self._validate()
        self._calculate_tip()
        self._print_output()


if __name__ == '__main__':
    TipCalculator().proceed()
