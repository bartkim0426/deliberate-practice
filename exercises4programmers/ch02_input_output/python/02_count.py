'''
pseudocode

validate_input
    if message is None
        return False
end

get_input
    get input from standard input
    validate_input
end

main
   char = get_input 
   create message with len of char
   print out message
end
'''


def get_input() -> str:
    '''
    get input from standard input.
    repeatedly get input if nothing entered
    '''
    char = ''
    while not char:
        char = input('What is the input string? ')
    return char


def count_input_char():
    '''print out count of input char'''
    input_char = get_input()
    print(f'{input_char} has {len(input_char)} characters.')


if __name__ == '__main__':
    count_input_char()
