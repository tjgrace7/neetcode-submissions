# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 == None and node2 == None:
                return None
            node = TreeNode()
            if node1 and node2:
                node.val = node1.val + node2.val
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)
            elif node1:
                node.val = node1.val
                node.left = dfs(node1.left, None)
                node.right = dfs(node1.right, None)
            else:
                node.val = node2.val
                node.left = dfs(None, node2.left)
                node.right = dfs(None, node2.right)
            return node

        
        return dfs(root1, root2)
     