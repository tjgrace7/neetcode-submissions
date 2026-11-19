class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {}
        nums[n] = 1
        def sumSquares(n) -> int:
            num = str(n)
            ans = 0
            for digit in num:
                dig = int(digit)
                ans += dig **2
            return ans
        while n != 1:
            n = sumSquares(n)
            nums[n] = nums.get(n, 0) +1
            if nums[n] > 1:
                return False
        return True
