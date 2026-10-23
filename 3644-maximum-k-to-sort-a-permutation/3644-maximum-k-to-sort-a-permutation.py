class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res=-1
        for i in range(len(nums)):
            if nums[i]!=i:
                res=res&nums[i]
                if res==0:
                    return 0
        return max(res,0)
        