# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def Walk(node, node2):
            if not node or not node2:
                if not node and not node2:
                    return True
                return False             
            if node.val != node2.val:
                return False            
            
            if not Walk(node.left, node2.left):
                return False
            if not Walk(node.right, node2.right):
                return False
            return True
            
        return Walk(p, q)
