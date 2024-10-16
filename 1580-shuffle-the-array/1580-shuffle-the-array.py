class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        n1 = nums[0:n]
        n2 = nums[n:]
        n3 = []
        for i in range(n):
            n3.append(n1[i])
            n3.append(n2[i])
        return n3