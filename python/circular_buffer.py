class CircularBuffer:
    def __str__(self):
        return f'{self.buffer}'

    def __iter__(self):
        '''
        그냥 buffer는 index가 0부터 순서대로 나오지만
        이렇게 iter를 구현하면 실제 다음에 제거하기 원하는 순서 (low -> high)대로 나오는것을 볼 수 있다

        >>> c = CircularBuffer(5)
        >>> for i in range(1, 6):
        ...     c.add(i)
        >>> c.add(6)
        >>> c.buffer
        [6, 2, 3, 4, 5]
        >>> c
        [2, 3, 4, 5, 6]
        '''
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx+1) % self.size
            num -= 1
    
    def __repr__(self) -> str:
        if self.isEmpty():
            return 'cb:[]'
        else:
            # iterator에서 읽어서 repr 해줌
            return 'cb:[' + ','.join(map(str, self)) + ']'

    def __init__(self, size: int):
        """contruct fixed size buffer"""
        self.size = size
        self.buffer = [None]*size
        self.low = 0
        self.high = 0
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def add(self, value):
        if self.isFull():
            # if self.low ends up to self.size-1, 0
            self.low = (self.low+1) % self.size
        else:
            self.count += 1

        self.buffer[self.high] = value
        self.high = (self.high+1) % self.size

    def remove(self):
        if self.count == 0:
            raise Exception("Circular buffer is empty")
        value = self.buffer[self.low]
        self.low = (self.low+1) % self.size
        self.count -= 1
        return value
