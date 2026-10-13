class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.tail = Node(-1)
        self.head = Node(-1, self.tail)

    
    def get(self, index: int) -> int:
        node = self.head.next
        idx = 0
        while node != self.tail:
            if idx == index:
                break
            node = node.next
            idx +=1
        if node != self.tail:
            return node.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        tmp = self.head.next
        self.head.next = Node(val, tmp)


    def insertTail(self, val: int) -> None:
        insertNode = Node(val, self.tail)
        node = self.head
        while node.next != self.tail:
            node = node.next
        node.next = insertNode

    def remove(self, index: int) -> bool:
        idx = 0
        node = self.head.next
        prev = self.head
        while node != self.tail:
            if idx == index:
                prev.next = node.next
                break
            prev = node
            node = node.next
            idx +=1
        if node == self.tail:
            return False
        else: 
            return True



    def getValues(self) -> List[int]:
        arr = []
        node = self.head.next
        while node != self.tail:
            arr.append(node.val)
            node = node.next
        return arr
