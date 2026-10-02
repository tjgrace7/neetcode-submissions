class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        k = 1
        while low <= high:
            hours = 0            
            mid = (low+high)//2
            for p in piles:
                if p <= mid:
                    hours +=1
                else:
                    hours += math.ceil(p/mid)
                if hours > h:
                    low = mid+1
                    break
            if hours <= h: 
                high = mid-1
                k = mid

        return k

        
                