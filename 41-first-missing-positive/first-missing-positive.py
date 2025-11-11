class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        taken = set()

        smallest_positive_int = 1

        for i in range(len(nums)):
            if(nums[i] < 0):
                continue
            taken.add(nums[i])
            if(nums[i] == smallest_positive_int):
                while(smallest_positive_int in taken):
                    smallest_positive_int += 1
        return smallest_positive_int