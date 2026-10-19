# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if not node:
            return
        right = None
        left = None
        if node.right:
            self.invertTree(node.right)
            right = node.right
        if node.left:
            self.invertTree(node.left)
            left = node.left
        node.left = right
        node.right = left
        return root

            