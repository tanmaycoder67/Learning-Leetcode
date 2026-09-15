class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wido_sum=sum(nums[:k])
        maxy=wido_sum
        for i in range(k,len(nums)):
            wido_sum=wido_sum+nums[i]-nums[i-k]
            maxy=max(maxy,wido_sum)
        return maxy/k

        