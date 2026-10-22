class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balon"
        count = 0
        res = {}
        for char in text:
            if char in target:
                res[char] = res.get(char, 0) + 1
            if res.get('b', 0) >=1 and res.get('a', 0) >= 1 and res.get('l',0) >=2 and res.get('o', 0) >=2 and res.get('n', 0) >=1:
                count +=1
                res['b'] -=1
                res['a'] -=1
                res['l'] -=2
                res['o'] -= 2
                res['n'] -=1

        return count
