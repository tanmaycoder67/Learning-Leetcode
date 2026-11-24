class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        we=[]
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            print(start,i)
            we.append(sum(nums[start:i+1]))
        return (sum(we))
        