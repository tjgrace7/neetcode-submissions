class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
            if len(res) < k and num not in res:
                res.append(num)
            for j in range(len(res)):
                if mp[num] > mp[res[j]] and num not in res:
                    res[j] = num
    

        return res