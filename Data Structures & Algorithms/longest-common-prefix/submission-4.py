class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            if len(s) < len(prefix):
                prefix = prefix[:len(s)]
            if len(s) == 0:
                prefix = ""
            i = 0
            while i < len(s) and i < len(prefix):
                if s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
                i +=1
        return prefix
        
        