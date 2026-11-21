class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        actual = sorted(set(nums))

        for i in range(len(actual)):
            nums[i] = actual[i]

        return len(actual)