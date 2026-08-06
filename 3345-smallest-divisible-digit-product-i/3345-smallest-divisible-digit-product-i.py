class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            e=1
            for i in str(n):
                e=e*int(i)
            if e%t==0:
                return(n)
                break
            else:
                n=n+1
            
        