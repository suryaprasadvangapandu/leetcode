class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l1 = []
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                l1.append(count)
                count = 0

        l1.append(count)
        return max(l1)