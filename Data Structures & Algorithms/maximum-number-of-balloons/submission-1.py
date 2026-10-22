class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26
        for c in text:
            freq[ord(c)-ord('a')] +=1
        return min(freq[0], freq[1], freq[11]//2, freq[13], freq[14]//2)