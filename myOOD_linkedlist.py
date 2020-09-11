class LinkedList:
    def __init__(self):
        self.dummy = Node(None)
        self.length = 0
    def __len__(self):
        return self.length
    def __iter__(self):
        n = self.dummy.next
        while n:
            yield n.val
            n = n.next

    hello_val = 1

    @staticmethod
    def hello():
        print("Hello: ", LinkedList.hello_val)

    def print(self):
        n_node = self.dummy.next
        while n_node:
            print(n_node.val)
            n_node = n_node.next

    def append(self, val):
        n_node = self.dummy
        while n_node.next != None:
            n_node = n_node.next
        node = Node(val)
        n_node.next = node
        self.length += 1

    def clear(self):
        self.dummy.next = None
        self.length = 0 

    def copy(self):
        nl = LinkedList()
        n = self.dummy.next
        while n:
            nl.append(n)
            n = n.next
        return nl

    def count(self, val):
        n = self.dummy.next
        cnt = 0
        while n:
            if n.val == val:
                cnt += 1
            n = n.next
        return cnt

    def extend(self, lis):
        for l in lis:
            self.append(l)

    def index(self, val):
        n = self.dummy.next
        idx = 0
        while n:
            if n.val == val:
                return idx
            n = n.next
            idx += 1
        return None

    def insert(self, ele, pos):
        node = Node(ele)
        if pos == 0:
            node.next = self.dummy.next
            self.dummy.next = node
            self.length += 1
            return

        n = self.dummy.next
        idx = 1
        while n.next:
            if idx == pos:
                node.next = n.next
                n.next = node
                self.length += 1
                return
            idx += 1
            n = n.next
        if pos == idx:
            n.next = node
            self.length += 1
            return

    def pop(self, pos):
        n = self.dummy.next
        if pos == 0:
            if n.next:
                self.dummy.next = n.next
                self.length -= 1
            return
        idx = 1
        while n.next:
            if idx == pos:
                n.next = n.next.next
                self.length -= 1
                return
            idx += 1
            n = n.next
    
    def remove(self, val):
        h = self.dummy

        while h.next:
            if h.next.val == val:
                h.next = h.next.next
                self.length -= 1
            else:
                h = h.next

    def reverse(self):
        n = self.dummy.next
        prev = None
        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp
        self.dummy.next = prev

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

