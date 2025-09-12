class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        map2 = {}
        if(len(s) != len(t)):
            return False
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 0

        for char in t:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 0
        return (map == map2)

        
        
