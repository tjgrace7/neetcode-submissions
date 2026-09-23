class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        m = 0
        for n in nums:
            if n == 1: 
                c+=1
                if c > m: m = c
            else: c = 0
        return m