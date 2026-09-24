class MyNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        i = 0
        node = self.head
        while i < index:
            if node == None:
                return -1
            node = node.nxt
            i += 1
        if node == None:
            return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        node = MyNode(val=val)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.nxt = self.head
            self.head.prev = node
            self.head = node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        node = MyNode(val=val)
        if self.tail == None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node
        self.size +=1 

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = MyNode(val)
        if index > self.size:
            return
        node = self.findNode(index)
        if node == None:
            self.addAtTail(val)            
        elif node == self.head:
            self.addAtHead(val)
        else:
            newNode.prev = node.prev
            newNode.nxt = node
            node.prev.nxt = newNode
            node.prev = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        node = self.findNode(index)
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.nxt = None 
    
        elif node == self.head:
            self.head = self.head.nxt
            self.head.prev = None
        else:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
        self.size -=1
    def findNode(self, index: int) -> MyNode:
        node = None
        if index < self.size/2:
            i = 0
            node = self.head
            while i < index:
                node = node.nxt
                i += 1
        elif index >= self.size:
            return None
        else:
            i = self.size-1
            node = self.tail
            while i > index:
                node = node.prev
                i -= 1
        return node
    def Display(self):
        node = self.head
        print("Display Order")
        while node is not None:
            print(node.val)
            node = node.nxt

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)