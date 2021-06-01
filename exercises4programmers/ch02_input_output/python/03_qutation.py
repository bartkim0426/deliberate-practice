'''
pseudocode

get_input
    get input from stdin
end

print_quotation
    quote = get_input('What is the quote? ')
    person = get_input('Who said it? ')
    message = person + " says, " + "\"" + quote + "\""
    print(message)
end
'''


def get_input(question: str) -> str:
    '''Get input from stdin with print out question'''
    return input(question)


def print_quotation():
    quote = get_input('What is the quote? ')
    person = get_input('Who said it? ')
    message = person + " says, " + "\"" + quote + "\""
    print(message)


quotation: dict = {
    'Obi-Wan Kenobi': "These aren't the droids you're looking for",
}


def print_quotation_from_data():
    for person, quote in quotation.items():
        message = person + " says, " + "\"" + quote + "\""
        print(message)


if __name__ == '__main__':
    print_quotation()
