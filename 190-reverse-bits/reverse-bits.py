class Solution:
    def reverseBits(self, n: int) -> int:
        bin = format(n,"032b")
        rev = bin[::-1]
        num = int(rev, 2)
        return num


        