class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_palindromes = 0
        for i in range(len(s)):
            num_palindromes = num_palindromes + self.check_palindromes(s, i, i)
            num_palindromes = num_palindromes + self.check_palindromes(s, i, i+1)

        return num_palindromes

    def check_palindromes(self, s, left, right):
        num_palindromes = 0
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left = left - 1
            right = right + 1
            num_palindromes = num_palindromes + 1

        return num_palindromes

# 1. loop through each character in s
# for each character, check the number of 