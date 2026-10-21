class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(lo, high):
            if lo > high:
                return None
            mid = (lo + high)//2
            return TreeNode(nums[mid], build(lo, mid-1), build(mid+1, high))
        return build(0, len(nums)-1)