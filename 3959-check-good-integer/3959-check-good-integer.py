class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        de=str(n)
        squaare=0
        sunn=0
        for i in de:
            sunn=sunn+int(i)
            squaare=squaare+(int(i)*int(i))
        if squaare-sunn>=50:
            return True
        else:
            return False
        