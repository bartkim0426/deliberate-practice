'''
pseudocode

get_input
    get input from stdin for specific question
end

mad_libs
    noun = get_input('Enter a noun: ')
    verb = get_input('Enter a verb: ')
    adjective = get_input('Enter a adjective: ')
    adverb = get_input('Enter a adverb: ')

    story = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    print(story)
end
'''


def get_input(question: str) -> str:
    '''get input from stdin for specific question'''
    return input(question)


def mad_libs():
    noun = get_input('Enter a noun: ')
    verb = get_input('Enter a verb: ')
    adjective = get_input('Enter a adjective: ')
    adverb = get_input('Enter a adverb: ')

    story = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    print(story)


if __name__ == '__main__':
    mad_libs()
