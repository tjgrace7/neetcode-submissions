# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(right_height-left_height) <= 1
            )
            height = 1 + max(right_height, left_height)
            return balanced, height
        balanced, _ = dfs(root)
        return balanced
       
