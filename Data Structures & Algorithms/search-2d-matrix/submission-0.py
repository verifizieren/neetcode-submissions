class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalLen = sum(len(row) for row in matrix) -1
        rowCnt = len(matrix)
        rowLen = len(matrix[0])
        l = 0
        r = totalLen

        while l <= r:
            m = (l + r) // 2
            
            row = m // rowLen
            col = m % rowLen

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m -1

        return False