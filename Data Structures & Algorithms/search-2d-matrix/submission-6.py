class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = (n*m) -1

        while left <= right:
            mid = (left+right)//2

            r = mid // m
            c = mid % m

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False