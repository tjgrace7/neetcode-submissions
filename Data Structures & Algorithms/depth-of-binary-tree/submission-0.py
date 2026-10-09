# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q = deque([root])
        while q:
            depth +=1 
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    return 0
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return depth