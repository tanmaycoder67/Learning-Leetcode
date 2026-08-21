class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1=list(set(nums))
        nums1.sort()
        if len(nums1)>=3:
            return(nums1[-3])
        else:
            return(max(nums1))
        