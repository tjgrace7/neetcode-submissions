class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = prices[0]
        value = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i]-low > value:
                value = prices[i] -low
                

        return value

