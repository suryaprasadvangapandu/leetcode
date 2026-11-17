class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        l1=[]
        for i in nums:
            count =0
            for j in range(len(nums)):
                if(i>nums[j]):
                    count+=1
            l1.append(count)
        return l1
                    
