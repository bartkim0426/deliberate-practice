wordkey = '\n'  # can be any character not 'a..z'


class PrefixTree:
    '''
    Data structure that compactly stores strings
    # example: init, in
    {
        'i': {
            'n': {
                'i': {
                    't': {
                        'isEnd': True
                    }
                },
                'isEnd': True  #?
            }
        }
    }
    '''
    def __init__(self, *args):
        self.head = {}

        if args:
            for arg in args:
                self.add(arg)

    def add(self, value: str) -> bool:
        '''Add avlue to prefix tree. Return TRUE if updated'''
        d = self.head

        while len(value) > 0:
            c = value[0]
            if c not in d:
                d[c] = {}
            d = d[c]
            value = value[1:]
        if wordkey in d:
            return False
        d[wordkey] = True
        return True

    def __contains__(self, value: str):
        '''
        determine if value in prefix tree

        >>> d = PrefixTree()
        >>> d.add('in')
        >>> d.add('inch')
        >>> 'in' in d
        True
        >>> 'inc' in d
        False
        >>> 'inch' in d
        True
        ''' 
        d = self.head
        while len(value) > 0:
            c = value[0]
            if c not in d:
                return False
            d = d[c]
            value = value[1:]
        return wordkey in d

    def __repr__(self):
        return f'{self.head}'

#     def __iter__(self):
#         '''Make PrefixTree iterable for words'''
#         d = self.head
#         stack = [d]
# 
#         while stack:
#             while len(values):
#                 c = d[next_word]
# 
# 
#         for k, v in d.items():
#             word = k
#             value = v
#             while len(value) > 0:
# 
#             # if wordkey in d
#             yield word
