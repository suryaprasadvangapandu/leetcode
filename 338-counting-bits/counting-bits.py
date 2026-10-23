class Solution:
    def countBits(self, n: int) -> list[int]:
        l1=[]
        for i in range(n+1):
            binary = ""
            count=0
            while i > 0:
                rem = i % 2
                if(rem==1):
                    count+=1
                i = i // 2
            l1.append(count)
        return l1