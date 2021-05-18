def fibonacci(n):
    '''리스트로 구현된 피보나치'''
    a = b = 1
    result = [a, b]
    while n > 2:
        n = n - 1
        a, b = b, a + b
        result.append(b)
    return result


def fibonacci_generator(n):
    '''제너레이터로 구현한 피보나치'''
    a = b = 1
    yield a
    yield b
    while n > 2:
        n = n - 1
        a, b = b, a + b
        yield b
