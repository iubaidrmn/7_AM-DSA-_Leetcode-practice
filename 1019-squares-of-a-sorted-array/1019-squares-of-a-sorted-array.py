class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range (len(nums)):
        #     sq_array = [x**2 for x in nums]
        # sq_array.sort()
        # return sq_array
        n = len(nums)
        # Result array to hold the squared numbers
        sq_array = [0] * n
        left, right = 0, n - 1
        # Pointer for filling the result array from the end
        index = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sq_array[index] = nums[left] ** 2
                left += 1
            else:
                sq_array[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return sq_array