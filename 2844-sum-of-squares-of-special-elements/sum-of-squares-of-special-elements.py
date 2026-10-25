class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            if(len(nums) % (i+1)==0):
                sum +=nums[i]**2
        return sum
