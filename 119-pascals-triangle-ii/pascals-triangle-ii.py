class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        old_row = [1]
        new_row = [1]
        for i in range (1, rowIndex + 1):
            new_row = [1] * (i+1)
            for j in range (1, i):
                new_row[j] = old_row[j-1] + old_row[j]

            old_row = new_row

        return  new_row

