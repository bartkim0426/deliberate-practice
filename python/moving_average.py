from circular_buffer import CircularBuffer


class MovingAverage(CircularBuffer):
    '''
    Implementation of a moving average by extending CircularBuffer
    '''
    def __init__(self, size):
        CircularBuffer.__init__(self, size)
        self.total = 0

    def get_average(self):
        '''return moving average (zero if no elements)'''
        if self.count == 0:
            return 0
        return self.total / self.count

    def add(self, value):
        '''total을 계산하기 위한 add'''
        if self.isFull():
            delta = -self.buffer[self.low]
        else:
            delta = 0
        delta += value
        self.total += delta
        CircularBuffer.add(self, value)

    def remove(self):
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed

    def __repr__(self):
        if self.isEmpty():
            return 'ma:[]'
        return 'ma:[' + ','.join(map(str, self)) + ']:' + str(self.get_average())
