class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        count = 0
        final_count = 0
        chars = set()
        left = 0
        right = 0

        for right in range(len(s)):

            while(s[right] in chars):
                chars.remove(s[left])
                left = left + 1
            chars.add(s[right])
            if ((right - left) + 1 > final_count):
                final_count = (right - left) + 1
        return final_count
