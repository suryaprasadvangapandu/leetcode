class Solution:
    def minElement(self, nums: List[int]) -> int:
        l1 =[]
        for i in nums:
            sum = 0
            for j in str(i):
                sum = sum+int(j)
            l1.append(sum)
        return min(l1)
            
