class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evn=0
        odd=1
        final=[0]*len(nums)
        for i in range (len(nums)):
            if nums[i]%2==0:
                final[evn]=nums[i]
                evn+=2

            else:
                final[odd]=nums[i]
                odd+=2
        return(final)

                