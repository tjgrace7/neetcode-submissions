class Node:
    def __init__(self, val):
        self.value =  val
        self.next = None
class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None


    def push(self, x: int) -> None:
        node = Node(x)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def pop(self) -> int:
        prev = None
        curr = self.head
        while curr is not None:
            if curr == self.tail:
                self.tail = prev
                if prev == None: self.head = None
                return curr.value
            prev = curr
            curr = curr.next
        return 0

    def top(self) -> int:
        return self.tail.value


    def empty(self) -> bool:
        if self.head == None:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()