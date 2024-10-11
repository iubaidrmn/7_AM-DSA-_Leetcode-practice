class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=list(nums)
        nums.extend(ans)
        return nums
