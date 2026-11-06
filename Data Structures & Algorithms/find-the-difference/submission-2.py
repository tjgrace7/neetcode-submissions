class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for char in s:
            m[char] = m.get(char, 0) + 1 
        print(m)
        for char in t:
            if char not in m or m[char] == 0:
                return char
            m[char] -=1