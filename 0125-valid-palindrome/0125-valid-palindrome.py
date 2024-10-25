import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        new = result.lower()
        reversed_text = ''.join(reversed(new))
        if reversed_text == new:
            return True
        else:
            return False