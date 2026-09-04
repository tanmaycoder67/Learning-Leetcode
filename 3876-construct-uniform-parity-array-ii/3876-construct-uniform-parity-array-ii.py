class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        smallestNum = nums1[0]
        for it in nums1:
            smallestNum = min(smallestNum, it)

        if smallestNum % 2 == 1:
            return True

        for it in nums1:
            if it % 2 == 1:
                return False

        return True

        