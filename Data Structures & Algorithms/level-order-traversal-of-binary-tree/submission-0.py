# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        quene = deque()
        if root:
            quene.append(root)
        arr = []
        while len(quene) >0:
            inner = []
            for i in range(len(quene)):
                curr = quene.popleft()
                inner.append(curr.val)
                if curr.left:
                    quene.append(curr.left)
                if curr.right:
                    quene.append(curr.right)
            arr.append(inner)
        return arr