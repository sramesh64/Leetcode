class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]


        def rob_subset(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if(len(nums) == 0):
                return 0
            if(len(nums) == 1):
                return nums[0]
            if(len(nums) == 2):
                return max(nums[0], nums[1])
            if(len(nums) == 3):
                return max(nums[0] + nums[2], nums[1])
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = dp[0] + nums[2]
            for i in range (3, len(nums)):
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])

            return max(dp[len(nums)-1], dp[len(nums)-2]) 

        return max (rob_subset(nums[:len(nums)-1]), rob_subset(nums[1:len(nums)]))
        

