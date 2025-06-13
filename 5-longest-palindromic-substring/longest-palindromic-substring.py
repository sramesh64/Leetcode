class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        left = 0
        right = 0
        final_left = '\0'
        final_right = '\0'
        for i in range(len(s)):
            left = i
            right = i
            
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            
            if (right - left + 1 > length):
                final_right = right
                final_left = left
                length = right - left + 1
            
            left = i
            right = i+1

            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            
            if (right - left + 1 > length):
                final_right = right
                final_left = left
                length = right - left + 1

        return s[final_left + 1:final_right]

