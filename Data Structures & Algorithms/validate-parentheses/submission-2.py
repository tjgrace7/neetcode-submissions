class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opn = ["(", "[", "{"]
        clsd = [")", "]", "}"]
        for char in s:
            if char in clsd:
                if not arr: return False
                i = clsd.index(char)
                if arr[-1] == opn[i]:
                    arr.pop()
                    continue
                elif arr[-1] in clsd: continue
                else: return False
            else:
                arr.append(char)
        return not arr

            