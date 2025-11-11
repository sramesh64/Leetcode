class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #. bin search to find the least index where target occurs
        # bin search from that index to end to find max index where target occurs
        #return both numbers
        if not nums:
            return [-1, -1]
        first_index = -1
        last_index = -1

        left = 0
        right = len(nums) - 1
        #bin search to find leftmost
        while(left < right):
            mid = (left + right) // 2

            if(nums[mid] < target):
                left = mid + 1

            else:
                right = mid
        #left is now the first occurence of target

        if(nums[left] != target):
            return [-1, -1]

        first = left
        right = len(nums) - 1

        #bin search to find rightmost
        while(left <= right):
            mid = (left + right) // 2

            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        last = right
        return [first, last]