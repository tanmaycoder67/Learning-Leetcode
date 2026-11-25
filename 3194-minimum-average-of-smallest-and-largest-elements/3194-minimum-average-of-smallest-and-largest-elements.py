class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        b=nums
        n=len(nums)//2
        avg=[]
        for i in range(n):
            r=min(b)
            e=max(b)
            avg.append((r+e)/2)
            b.remove(r)
            b.remove (e)
        return (min(avg))
                