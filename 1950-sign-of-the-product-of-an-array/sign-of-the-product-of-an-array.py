class Solution:
    def arraySign(self, nums: list[int]) -> int:
        mul = 1
        for i in nums:
            mul=mul*i
        if(mul>0):
            return 1
        elif(mul<0):
            return -1
        elif(mul==0) :
            return 0
