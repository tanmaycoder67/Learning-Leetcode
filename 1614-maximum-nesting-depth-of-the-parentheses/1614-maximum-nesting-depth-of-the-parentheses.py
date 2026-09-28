class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0   
        re = 0      

        for ch in s:
            if ch == "(":
                count += 1
                re = max(re, count)  
            elif ch == ")":
                count -= 1

        return (re)
        