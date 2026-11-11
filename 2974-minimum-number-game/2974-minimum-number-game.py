class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        final=[]
        for i in range(0,len(nums),2):
            arr.append((nums[i:i+2][::-1]))
        for i in arr:
            for j in i:
                final.append(j)
        return (final)
        