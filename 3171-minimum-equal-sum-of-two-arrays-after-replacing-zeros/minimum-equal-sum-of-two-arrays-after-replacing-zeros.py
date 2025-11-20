class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        sum1_with_zeros = sum1 + nums1.count(0)
        sum2_with_zeros = sum2 + nums2.count(0)

        if(nums1.count(0) == 0 and nums2.count(0) == 0):
            if(sum1 == sum2):
                return sum1
            return -1
        if(nums1.count(0) != 0 and nums2.count(0) != 0):
            return max(sum1_with_zeros, sum2_with_zeros)
        if(nums1.count(0) == 0):
            if(sum1 < sum2_with_zeros):
                return -1
            return sum1
        if(nums2.count(0) == 0):
            if(sum2 < sum1_with_zeros):
                return -1
            return sum2
            