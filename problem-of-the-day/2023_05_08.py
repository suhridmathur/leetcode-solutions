# https://leetcode.com/problems/matrix-diagonal-sum/description/
# 1572. Matrix Diagonal Sum


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        lcol = 0
        rcol = cols-1

        result = 0
        for row in range(rows):
            if lcol != rcol:
                result += (mat[row][lcol] + mat[row][rcol])
            else:
                result += mat[row][lcol]
            lcol += 1
            rcol -= 1

        return result
