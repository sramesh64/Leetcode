class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        a = set(nums)

        for i in range (len(nums)):
            if ((i not in a) and (i + 1 in a)): 
                return i

        return len(nums)