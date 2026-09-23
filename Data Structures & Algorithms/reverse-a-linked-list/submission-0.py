# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        currentNode = head
        nextNode = None
        previousNode = None
        while currentNode.next != None:
            nextNode = currentNode.next
            if currentNode == head:
                currentNode.next = None
            else: 
                currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            if currentNode.next == None:
                currentNode.next = previousNode
                break 
        return currentNode