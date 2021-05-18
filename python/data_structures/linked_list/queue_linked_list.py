class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

class QueueLinkedList:
    def __init__(self, *start):
        self.head = None
        self.tail = None

        for _ in start:
            self.append(_)

    def append(self, value):
        '''Add value to end of queue'''
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        '''Remove first value from queue'''
        if self.head is None:
            raise Exception('Queue is empty')
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def isEmpty(self):
        '''Determine if queue is empty'''
        return self.head == None

    def __iter__(self):
        '''Iterator of values in queue'''
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        return 'QueueLinkedList:[' + ','.join(map(str, self)) + ']'
