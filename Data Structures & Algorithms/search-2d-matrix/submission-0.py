class Solution:
    def computeRowCol(self, lenCols, pos):
        """
        0 1 2 3
        4 5 6 7
        8 9 10 11

        pos -> 8 is row 2, col 0
        """

        row = pos // lenCols
        col = pos % lenCols

        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenColumns = len(matrix[0])
        lenRows = len(matrix)

        left, right = 0, (lenColumns*lenRows)-1

        while left<=right:
            mid = (left+right) // 2
            row, col = self.computeRowCol(lenColumns, mid)

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                right = mid-1
            
            else:
                left = mid+1
        
        return False