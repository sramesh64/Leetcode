class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        lo, hi = 0, len(nums) - 1

        while(lo <= hi):
            mid = (lo + hi)//2
            if(nums[mid] == target):
                return mid
            elif(lo == hi):
                if(nums[lo] == target):
                    return lo
                return -1

            if (nums[mid] >= nums[lo]): #bottom half is sorted
                if (nums[lo] <= target <= nums[mid]):
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: #top half is sorted
                if (nums[mid] <= target <= nums[hi]):
                    lo = mid + 1
                else:
                    hi = mid - 1


