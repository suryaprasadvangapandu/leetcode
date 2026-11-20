class Solution:
    def firstUniqChar(self, s: str) -> int:
        d1={}
        for i in s:
            if(i in d1):
                d1[i] +=1
            else:
                d1[i]=1
        for i in d1:
            if(d1[i]==1):
                return s.index(i)
                break
        else:
            return -1
