class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums) -1
        left = 0
        mid = right / 2

        while(left != right):
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

            mid = (left+right)/2

        return nums[left]
        