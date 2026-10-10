class Solution:
    def reverse(self, x: int) -> int:  #-321
        sign = -1 if(x<0) else 1

        temp = abs(x) #321
        rev = 0
        while(temp>0):
            dig = temp%10
            rev = rev * 10 + dig
            temp//=10
        


        if(not (-2**31)<=rev*sign<=(2**31)-1):
            return 0


        return rev*sign

                
        