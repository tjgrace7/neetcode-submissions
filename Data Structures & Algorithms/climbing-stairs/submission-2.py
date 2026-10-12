class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        i = 2
        dp = [1, 2]
        while i < n:
            tmp = dp[1]
            dp[1] = dp[0]+dp[1]
            dp[0] = tmp
            i +=1
        return dp[1]