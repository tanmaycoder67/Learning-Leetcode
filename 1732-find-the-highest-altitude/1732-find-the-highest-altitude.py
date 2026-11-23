class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        count=0
        red=[0]
        for i in gain:
            count=count+i
            red.append(count)
        return(max(red))
        