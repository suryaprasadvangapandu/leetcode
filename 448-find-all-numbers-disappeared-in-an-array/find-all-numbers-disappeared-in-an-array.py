class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        dis = []
        l1 = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in l1:
                dis.append(i)

        return dis