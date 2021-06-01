'''
pseudocode

get_int_input
end

calculate_retirement
    current_age = get_int_input('What is your current age? ')
    retire_age = get_int_input('At what age would you like to retire? ')

    get current year from python
    left_years = retire_age - current_age

    message = f"You have {left_years} years left until you can retire.\nIt's {current_year}, so you can retire in {current_year + left_years}."
    print(message)
end
'''
from datetime import datetime


def get_int_input(question: str) -> str:
    result = ''
    while not result.isnumeric():
        result = input(question)
    return result


def calculate_retirement():
    current_age: int = int(get_int_input('What is your current age? '))
    retire_age: int = int(get_int_input('At what age would you like to retire? '))

    current_year: int = datetime.now().year
    left_years: int = retire_age - current_age

    if left_years <= 0:
        print('Congratulations! You are already retired!')
        return

    message = f"You have {left_years} years left until you can retire.\nIt's {current_year}, so you can retire in {current_year + left_years}."
    print(message)


if __name__ == '__main__':
    calculate_retirement()
