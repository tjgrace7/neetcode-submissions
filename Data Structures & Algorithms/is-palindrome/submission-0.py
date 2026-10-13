class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        end = len(s)-1
        start = 0
        for i in range(len(s)):
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

            
               
            