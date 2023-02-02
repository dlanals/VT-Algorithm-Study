class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])

        zero_r, zero_c = set(), set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_r.add(r)
                    zero_c.add(c)
        
        for r in range(m):
            for c in range(n):
                if r in zero_r or c in zero_c:
                    matrix[r][c] = 0