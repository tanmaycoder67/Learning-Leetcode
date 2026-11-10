class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum = float('-inf')
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    maximum=max(maximum, (nums[i] - nums[j]) * nums[k])
        if maximum<0:
            return(0)
        else:
            return (maximum)
        