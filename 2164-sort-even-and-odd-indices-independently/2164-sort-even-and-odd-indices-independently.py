class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        re=[]
        ld=[]
        final=[0]*len(nums)
        for i in range(0,len(nums),2):
            re.append(nums[i])
        # print(re)
        for i in range(1,len(nums),2):
            ld.append(nums[i])
        # print(ld)
        re.sort()
        ld.sort(reverse=True)
        od=ld
        # print(od)
        we=re
        # print(we)
        e=0
        o=0
        for i in range(len(nums)):
            if i % 2 == 0:
                final[i] = re[e]
                e += 1
            else:
                final[i] = ld[o]
                o += 1

        return final
        