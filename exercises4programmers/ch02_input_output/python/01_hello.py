'''
psuedocode

get_name
    name = get name from standard input 
    return name
end

concat_hello
    set message
    Hello, + name, nice to meet you!
    return message
end

print_out
    print message
end

main
    name = get_name
    message = concat_hello(name)
    print_out(name)
end
'''

def get_name() -> str:
    '''Get name from standard input'''
    return input('What is your name? ')

def concat_hello(name: str) -> str:
    '''Concat hello message with name'''
    return f'Hello, {name}, nice to meet you!'


def main():
    print(concat_hello(get_name()))


if __name__ == '__main__':
    main()
