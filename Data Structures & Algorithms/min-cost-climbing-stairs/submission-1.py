class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * (n)
        def recursive(c, i):
            if i > n:
                return 10
            elif i == n:
                return 0
            print(cache[i])
            if cache[i] != -1:
                return cache[i]
            cache[i] = min(recursive(c, i +1), recursive(c, i + 2))
            cache[i] += cost[i]
            return cache[i]
        return min(recursive(0, 0), recursive(0, 1))