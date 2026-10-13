class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l1 = []
        for i in range(len(nums)+1):
            l1.append(i)
        for i in l1:
            if(i not in nums ):
                return i