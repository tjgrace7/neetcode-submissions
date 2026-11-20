class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0]
        for i in range(1, len(nums)):
            if (prev % 2 == 0 and nums[i] % 2 == 0) or (prev %2 != 0 and nums[i] %2 != 0):
                return False
            prev = nums[i]
        return True
            
                