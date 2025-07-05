class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = set()

        for i in range (len(nums) - 2):
            a = i + 1
            b = len(nums)-1
            while(a < b):
                if ((nums[i] + nums[a] + nums[b]) > 0):
                    b = b - 1
                elif ((nums[i] + nums[a] + nums[b]) < 0):
                    a = a + 1
                elif((nums[i] + nums[a] + nums[b]) == 0):
                        triplet = tuple(sorted([nums[i], nums[a], nums[b]]))
                        triplets.add(triplet)
                        a = a + 1
                        b = b - 1
                else:
                    a = a + 1
                    b = b - 1

        return list(triplets)

