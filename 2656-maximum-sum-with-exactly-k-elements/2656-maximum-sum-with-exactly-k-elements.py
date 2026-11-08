class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        f=max(nums)

        sum=0
        for i in range(k):
            sum=sum+f
            f=f+1
        return(sum)
        