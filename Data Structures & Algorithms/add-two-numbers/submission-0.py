# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        node = l1
        node2 = l2
        arr2 = []
        num1 = ""
        num2 = ""
        while node is not None:
            arr1.append(node.val)
            node = node.next
        while node2 is not None:
            arr2.append(node2.val)
            node2 = node2.next
        for i in range(len(arr1)-1, -1, -1):
            num1 = num1 + num1.join(str(arr1[i]))
        for i in range(len(arr2)-1, -1, -1):
            num2 = num2 + num2.join(str(arr2[i]))
        comb = int(num1) + int(num2)
        nxt = None
        for char in str(comb):
            node = ListNode(int(char))
            if nxt is not None:
                node.next = nxt
            nxt = node
        return nxt