class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        cnt0 = 0
        
        for x in nums:
            xor ^= x
            if x == 0:
                cnt0 += 1
        
        if xor != 0:
            return n
        if cnt0 == n:
            return 0
        return n - 1