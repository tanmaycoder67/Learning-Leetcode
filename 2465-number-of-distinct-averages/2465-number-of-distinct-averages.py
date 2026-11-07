class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        saw=[]
        while len(nums)!=0:
            avg=0
            for i in nums:
                m=max(nums)
                nums.remove(m)
                mi=min(nums)
                nums.remove(mi)
                avg=(m+mi)/2
                saw.append(avg)

        return (len(set(saw)))
                