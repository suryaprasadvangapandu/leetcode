class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        for i in range(n-2,-1,-1):
            m = len(triangle[i])
            for j in range(m):
                left  = triangle[i+1][j]
                right  = triangle[i+1][j+1]
                triangle[i][j] += min(left,right)
        return triangle[0][0]


                