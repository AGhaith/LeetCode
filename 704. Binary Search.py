
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        middle = length//2
        if length == 0:
            return -1
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.search(nums[:middle],target)
        else:
            return self.search(nums[middle+1:],target)
# Test the function
testarray = [-1, 0, 3, 5, 9, 12]
sol = Solution()
print(sol.search(testarray, 3))  # Output should be -1 (not found)