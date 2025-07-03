class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        curr_min = nums[0]
        max_num = curr_max

        for i in range(1, len(nums)):
            prev_max = curr_max
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * curr_min)
            if(curr_max > max_num):
                max_num = curr_max

        return max_num


