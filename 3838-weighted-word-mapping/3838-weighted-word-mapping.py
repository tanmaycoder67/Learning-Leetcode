class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            mod_val = total % 26
            ans += chr(ord('z') - mod_val)
        
        return ans
        