class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l1=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] == target):
                l1.append(i)
        return  l1
