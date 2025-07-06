class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parantheses_matches = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if(char == '(' or char == '{' or char == '[' ):
                stack.append(char)
            elif(len(stack) == 0):
                return False
            else:
                bracket = stack.pop()
                if (parantheses_matches[bracket] != char):
                    return False
        
        if len(stack) != 0: return False
        return True



#use a stack

