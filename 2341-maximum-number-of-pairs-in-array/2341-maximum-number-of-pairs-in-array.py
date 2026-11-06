class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        seen={}
        pair=0
        for i in nums:
            if i in seen:
                seen[i]+=1
                pair+=1
                del seen[i]
            else:
                seen[i]=1
        return ([pair, len(seen)])
        