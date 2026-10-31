import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = 0
        sumeven = 0
        i = 1

        while i <= n:
            sumodd = sumodd + (2 * i - 1)
            sumeven = sumeven + (2 * i)
            i = i + 1

        return math.gcd(sumodd, sumeven)
