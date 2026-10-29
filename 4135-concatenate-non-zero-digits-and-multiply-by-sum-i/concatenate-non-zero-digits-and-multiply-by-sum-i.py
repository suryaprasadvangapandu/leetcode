class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num =''
        sum =0
        for i in str(n):
            if(i != '0'):
                num = num+i
                sum = sum+int(i)
        if(num==''):
            return 0

        return int(num)*sum
            