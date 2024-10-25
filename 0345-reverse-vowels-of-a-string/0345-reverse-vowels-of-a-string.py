class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk=[]#Create a stack
        
        for i in s:
            if i.lower() in "aeiou":
                stk.append(i)#Store vowel in stack
        
        rev=""#Create empty string
        
        for i in s:
            if i.lower() in "aeiou":
                rev+=stk.pop(-1)
            else:
                rev+=i
        
        return rev