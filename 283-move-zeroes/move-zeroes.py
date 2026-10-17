
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = []

        while 0 in nums:
            nums.remove(0)
            l1.append(0)

        nums[:] = nums + l1
