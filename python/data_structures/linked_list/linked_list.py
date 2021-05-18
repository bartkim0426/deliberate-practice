class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

    def checkInfinite(self):
        p1 = p2 = self
        while p1 != None and p2 != None:
            if p2.next == None:
                return False

            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        '''Add value to front of the list. O(1)'''
        self.head = LinkedNode(value, self.head)

    def remove(self, value):
        '''remove specific value from list. O(n)'''
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            last = n
            n = n.next
        return False

    def pop(self):
        '''Remove first value from list. O(1)'''
        if self.head is None:
            raise Exception('Empty list')
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        return 'LinkedList:[' + ','.join(map(str, self)) + ']'
