class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        l1=[]
        for i in range(left,right+1):
            temp =i
            count = 0
            while(temp>0):
                rem = temp%10
                if(rem!=0 and i%rem==0):
                    count+=1
                temp //=10
            if(count==len(str(i))):
                l1.append(i)
        return l1



