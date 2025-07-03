class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        nums.append([1])
        for i in range (1, numRows):
            numsinRow = [1] * (i+1)
            for j in range (1, i):
                numsinRow[j] = nums[i-1][j-1] + nums[i-1][j]
            nums.append(numsinRow)
        return nums

        