class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        se=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                se.append(i)
        return se

        