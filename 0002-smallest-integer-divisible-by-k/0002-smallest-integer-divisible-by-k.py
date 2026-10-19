class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k<=0:
            return -1
        elif k%2==0 or k%5==0:
            return -1
        else:
            ev=1%k
            l=1

            while ev!=0:
                ev=(ev*10+1)%k
                l=l+1
            return l
        