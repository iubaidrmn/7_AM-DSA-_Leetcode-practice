class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = set()

        for num in nums:
            if num in res: # duplicate exists
                return True
            res.add(num)
        return False