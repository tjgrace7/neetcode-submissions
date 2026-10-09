# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        curr = head
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        curr = head
        i = len(res)-1
        while i >= 0:
            if curr == None or res[i] != curr.val:
                return False
            curr = curr.next
            i -= 1
        return True