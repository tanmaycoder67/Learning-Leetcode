class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        s=str(num)
        for i in s:
            if num%int(i)==0:
                count=count+1
        return (count)

        