class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opn = ["(", "[", "{"]
        clsd = [")", "]", "}"]
        for char in s:
            if char in clsd and len(arr) > 0:
                i = clsd.index(char)
                if arr[-1] == opn[i]:
                    arr.pop()
                    continue
                elif arr[-1] in clsd: continue
                else: return False
            arr.append(char)
        if len(arr) > 0: return False
        return True

            