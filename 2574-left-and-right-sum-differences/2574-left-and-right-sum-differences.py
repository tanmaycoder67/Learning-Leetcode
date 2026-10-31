class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ri_sum=[0]
        le_sum=[]
        ans=[]
        
        for i in range(len(nums)-1):
            ri_sum.append(ri_sum[i]+nums[len(nums)-1-i])
        ri_sum=ri_sum[::-1]

        for i in range(len(nums)):
            le_sum.append(sum(nums[:i]))
        
        for j in range(len(nums)):
            ans.append(abs(le_sum[j]-ri_sum[j]))
        return ans
        