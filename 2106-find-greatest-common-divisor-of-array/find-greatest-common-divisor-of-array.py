import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        result  = math.gcd(smallest,largest)
        return result