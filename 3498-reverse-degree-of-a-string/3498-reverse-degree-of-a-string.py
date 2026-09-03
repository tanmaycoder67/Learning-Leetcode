class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
        
            pos = i + 1
            
            rev = 26 - (ord(s[i]) - ord('a'))
            total += pos * rev
        return total
