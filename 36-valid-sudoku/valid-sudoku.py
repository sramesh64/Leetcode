class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def find_box_num(row, col):
            return (row // 3) * 3 + (col // 3)
            
        rows = len(board)
        cols = len(board[0])

        #9 sets, one for each box
        #9 sets, one for each column. list of sets, list[i] corresponds to a set with the values in columns[i]
        #9 sets, one for each row. list of sets, list[i] corresponds to a set with the values in row[i]

        s_boxes = [set() for _ in range(9)]
        s_rows = [set() for _ in range(9)]
        s_cols = [set() for _ in range(9)]

        for row in range(rows):
            for col in range(cols):
                if(board[row][col] == "."):
                    continue

                box_num = find_box_num(row, col)
                char = board[row][col]
                if(char in s_boxes[box_num] or char in s_rows[row] or char in s_cols[col]):
                    return False
                s_boxes[box_num].add(char)
                s_rows[row].add(char)
                s_cols[col].add(char)
        return True
                