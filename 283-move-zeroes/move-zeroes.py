
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l1 = []

        for i in nums:
            if i != 0:
                l1.append(i)

        while len(l1) < len(nums):
            l1.append(0)

        nums[:] = l1
