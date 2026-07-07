class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_arr, right_arr = 0, len(matrix) - 1
        target_arr = []
        while left_arr <= right_arr:
            mid = (left_arr + right_arr) // 2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                target_arr = matrix[mid]
                break
            elif target < matrix[mid][0]:
                right_arr = mid-1
            elif target > matrix[mid][-1]:
                left_arr = mid+1
        
        left, right = 0, len(target_arr)-1

        while target_arr and left <= right:
            mid = (left + right) // 2
            if target == target_arr[mid]:
                return True
            elif target < target_arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return False