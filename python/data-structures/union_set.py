class Node:
    '''
    Node for using in DisjonitSet data structure.
    - default parent: Node(-1)
    '''
    def __init__(self, value: int, parent=None):
        self.value = value
        self.parent = parent


class DisjointSet:
    '''
    data structure for union set (disjoint-set, union-find)
    '''
    def __init__(self, n: int, sets: dict=None):
        '''initialize elements for the value of -1 default'''
        if sets:
            self.sets = sets
        else:
            self.sets = {
                i: Node(value=i, parent=Node(-1))
                for i in range(n)
            }

    def union(self, a: int, b: int):
        '''union a and b node'''
        a_node = self.sets[a]
        b_node = self.sets[b]

        if a_node.value < b_node.value:
            b_node.parent = a_node
        else:
            a_node.parent = b_node

    def isConnect(self, a: int, b: int) -> bool:
        '''
        return true if a and b node is connected
        - a is parent of b / b is parent of a
        - connected if a, b has same parent
        '''
        a_node = self.sets[a]
        b_node = self.sets[b]
        if a_node.parent == b_node or b_node.parent == a_node or \
            self.find_parent(a_node.value) == self.find_parent(b_node.value):
            return True
        return False

    def find_parent(self, n: int) -> Node:
        '''
        find final parent node. return self node if no parent.
        # TODO: save final parent as parent when find parent
        '''
        node = self.sets[n]
        # exit
        if node.parent.value == -1:
            return node
        else:
            node.parent = self.find_parent(node.parent.value)
        # recursive call
        return self.find_parent(node.parent.value)

    def isCycle(self) -> bool:
        '''if sets are all connected then return true'''
        # if all have same final parent then cycle
        parent_sets = set()
        for _, node in self.sets.items():
            parent = self.find_parent(node.value)
            parent_sets.add(parent)
            if len(parent_sets) > 1:
                return False
        return True
