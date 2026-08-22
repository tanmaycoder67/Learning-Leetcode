class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        digits = []
        while n> 0:
            digits.append(n % 10)  
            n//= 10               
        digits.reverse()
        c=sum(digits)
        se=1
        for i in range(len(digits)):
            se=se*digits[i]
        dew=c+se
        return dew != 0 and num % dew == 0
        