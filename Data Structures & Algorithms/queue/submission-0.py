class Node:
    def __init__(self, val: int, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.tail = Node(-1)
        self.head = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head

    def isEmpty(self) -> bool:
        if self.head.next ==self.tail:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        tmp = self.tail.prev
        node = Node(value, self.tail, tmp)
        self.tail.prev = node
        tmp.next = node





    def appendleft(self, value: int) -> None:
        tmp = self.head.next
        node = Node(value, tmp, self.head)
        self.head.next = node
        tmp.prev = node


    def pop(self) -> int:
        node = self.tail.prev
        if node == self.head:
            return -1
        self.tail.prev = node.prev
        node.prev.next = self.tail
        return node.val

    def popleft(self) -> int:
        node = self.head.next
        if node == self.tail:
            return -1
        self.head.next = node.next
        node.next.prev = self.head
        return node.val
