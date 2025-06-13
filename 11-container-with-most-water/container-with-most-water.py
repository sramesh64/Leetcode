class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = 0
        max_volume = 0
        i = 0
        j = len(height) - 1
        while i < j:
            volume = min(height[i], height[j]) * (j-i)
            if volume > max_volume:
                max_volume = volume
            if(height[i] <= height[j]):
                i = i + 1
            else:
                j = j - 1

        return max_volume
