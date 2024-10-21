class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # new = []
        # N = len(s) - 1
        # for i in range (N, -1, -1):
        #     new.append(s[i])
        # s = new
        
        
        
        s[:] = s[::-1]

