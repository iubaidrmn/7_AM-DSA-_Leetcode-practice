class Solution(object):
    def findLucky(self, arr):
        ans = -1
        arrset = set(arr)
        for i in arrset:
            count = arr.count(i)
            if count == i:
                ans = i
        return ans