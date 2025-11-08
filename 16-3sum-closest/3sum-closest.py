class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        closest_distance = abs(target - (nums[0] + nums[1] + nums[2]))
        best_sum = nums[0] + nums[1] + nums[2]

        for i in range (len(nums) - 2):
            a = i + 1
            b = len(nums) - 1

            while(a < b):
                curr_sum = nums[i] + nums[a] + nums[b]
                curr_distance = abs(target - curr_sum)
                if(curr_sum == target):
                    return curr_sum
                
                if(curr_distance < closest_distance):
                    closest_distance = curr_distance
                    best_sum = nums[i] + nums[a] + nums[b]
                if(curr_sum > target):
                    b -= 1
                if(curr_sum < target):
                    a += 1
            
        return best_sum