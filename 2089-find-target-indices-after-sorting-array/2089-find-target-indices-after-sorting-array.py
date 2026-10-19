class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        df=[]
        for i in range(0,len(nums)):
            if(nums[i]==target):
                df.append(i)
        return df
        