class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        l1 = []
        for i in range(1,len(nums)+1):
            l1.append(i)
        for i in nums:
            if(nums.count(i) == 2):
                duplicate = i
                break
        for i in l1:
            if(i not in nums):
                missing = i
                break
        return [duplicate,missing]
