class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r,c = len(matrix),len(matrix[0])

        for i in range(r):
            if matrix[i][0] <= target <= matrix[i][c-1]:
                left = 0
                right = c-1
                while left <= right:
                    mid = (left+right)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right -=1 
                    else:
                        left += 1
                return False
        return False