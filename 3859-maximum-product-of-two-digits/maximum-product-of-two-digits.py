class Solution:
    def maxProduct(self, n: int) -> int:
        l1 = []
        l2=[]
        for i in str(n):
            l1.append(int(i))
        for i in range(len(l1)):
            mul=1
            for j in range(i+1,len(l1)):
                mul = l1[i]*l1[j]
                l2.append(mul)
        return max(l2)
            
        