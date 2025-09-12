class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mult = 1
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            mult *= nums[i-1]
            answer[i] = mult
        
        mult = 1
        
        for i in range(len(nums) - 2, -1, -1):
            mult *= nums[i + 1]
            answer[i] *= mult

        return answer
