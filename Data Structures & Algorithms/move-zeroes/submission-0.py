class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i
        while i < len(nums):
            if nums[i] == 0:
                while j < len(nums) and nums[j] == 0:
                    j +=1
                if j < len(nums) and nums[j] != 0:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
            i +=1
            j = i
                

