class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while len(nums)!=0:
            p=list(set(nums))
            p.sort()
            for i in p:
                ans.append(i)
                nums.remove(i)
            
        return (ans)
        