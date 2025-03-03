class Solution(object):
    def binarySearch(self, arr, target2):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == target2:
                return True
            elif arr[mid] < target2:
                low = mid+1
            else:
                high = mid-1
        return False
    def searchMatrix(self, matrix, key):
        """
        :type matrix: List[List[int]]
        :type key: int
        :rtype: bool
        """

        rows = len(matrix)
        if rows == 0:
            return False
        middle_row = rows//2
        if matrix[middle_row][0] <= key <= matrix[middle_row][-1]:
            return self.binarySearch(matrix[middle_row], key)
        elif matrix[middle_row][0] > key:
            return self.searchMatrix(matrix[:middle_row], key)
        else:
            return self.searchMatrix(matrix[middle_row+1:], key)


matrix = [[1]]
target = 60
sol = Solution()
print(sol.searchMatrix(matrix, target))