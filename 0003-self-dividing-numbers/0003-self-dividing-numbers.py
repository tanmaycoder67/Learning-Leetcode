class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        we=[]

        for n in range(left,right+1):
            for j in str(n):
                if int(j)==0 or n % int(j) != 0:
                    break
            else:
                we.append(n)
        return we
        