class Solution:
    def average(self, salary: list[int]) -> float:
        sum = 0
        for i in salary:
            if(i!=min(salary) and i != max(salary)):
                sum = sum+i
        return sum/(len(salary)-2)
            


                