class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_r = 0
        high_r = len(matrix) - 1
        target_r = []
        while low_r <= high_r:
            mid_r = (low_r + high_r) // 2
            if matrix[mid_r][0] <= target <= matrix[mid_r][len(matrix[0])-1]:
                target_r = matrix[mid_r]
                break
            elif matrix[mid_r][0] > target:
                high_r = mid_r - 1
            elif matrix[mid_r][len(matrix[0])-1] < target:
                low_r = mid_r + 1
        
        low_c = 0
        high_c = len(target_r) -1

        while target_r and low_c <= high_c:
            mid_c = (low_c + high_c) // 2
            if target_r[mid_c] == target:
                return True
            elif target_r[mid_c] < target:
                low_c = mid_c + 1
            elif target_r[mid_c] > target:
                high_c = mid_c - 1
        
        return False