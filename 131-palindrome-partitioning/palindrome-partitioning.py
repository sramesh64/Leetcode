class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def backtrack(start, words):
            if(start == len(s)):
                result.append(words)
                return
            for ending in range (start + 1, len(s) + 1):
                substring = s[start:ending]
                if(is_palindrome(substring)):
                    backtrack(ending, words + [substring])



        def is_palindrome(a):
            return a == a[::-1]
            
        result = []
        backtrack(0, [])
        return result
