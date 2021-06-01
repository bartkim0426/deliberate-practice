'''
pseudocode

get_int_input
    validate input for only integer
    repeatedly enter input till integer is coming
end

simple_math
    first_number = get_int_input('What is the first number? ')
    second_number = get_int_input('What is the second number? ')
    make first, second number into int
    print out four arthmetical operations
end
'''


def get_int_input(question: str) -> str:
    '''get integer input. Repeatedly enter input if not integer'''
    result = ''
    while not result.isnumeric():
        result = input(question)
    return result


def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    return a // b


def simple_math():
    '''print out four arthmetical operations'''
    first: int = int(get_int_input('What is the first number? '))
    second: int = int(get_int_input('What is the second number? '))

    operations_msg: list = [
        f'{first} + {second} = {plus(first, second)}',
        f'{first} - {second} = {minus(first, second)}',
        f'{first} * {second} = {multiply(first, second)}',
        f'{first} / {second} = {divide(first, second)}',
    ]
    print('\n'.join(operations_msg))


if __name__ == '__main__':
    simple_math()
