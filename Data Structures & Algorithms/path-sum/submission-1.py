# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0
        def pathtoLeaf(node, targetSum):
            nonlocal sum
            if not node:
                return False
            sum += node.val
            if not node.left and not node.right and sum == targetSum:
                return True
            if pathtoLeaf(node.left, targetSum):
                return True
            if pathtoLeaf(node.right, targetSum):
                return True
            sum -=node.val
            return False
        return pathtoLeaf(root, targetSum)