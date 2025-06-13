class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)
        count = 0
        final_count = 0
        for number in numbers:
            if(number - 1 not in numbers):
                while(number in numbers):
                    number = number + 1
                    count = count + 1

            if count > final_count:
                final_count = count
            count = 0
        return final_count





# 1. put nums in a set (so we can search elements in O(1))
# 2. we want to loop through each number in the set, 
#     for each number:
#         if the consecutive number is present
#             increment count, check next numnber

#         else:
#             set count to 0, check next number
        
#         if count > final count, replace final count with count