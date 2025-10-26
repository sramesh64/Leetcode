class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        row = 0
        dir = 1
        rows = [''] * numRows
        for char in s:
            rows[row] += char

            if(row == numRows - 1):
                dir = -1
            elif(row == 0):
                dir = 1

            row += dir
        
        return ''.join(rows)

