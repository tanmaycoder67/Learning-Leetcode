class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak=[]
        valley=[]
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peak.append(nums[i])
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                valley.append(nums[i])
        return (sum(peak)-sum(valley))
        