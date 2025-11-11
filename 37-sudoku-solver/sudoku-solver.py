class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        s_boxes = [set() for _ in range(9)]
        s_rows = [set() for _ in range(9)]
        s_cols = [set() for _ in range(9)]

        # preload sets from the given board
        for r in range(9):
            for c in range(9):
                
                char = board[r][c]
                if(char == '.'):
                    continue
                    
                box_num = (r // 3) * 3 + (c // 3)
                s_boxes[box_num].add(char)
                s_rows[r].add(char)
                s_cols[c].add(char)
                


        def dfs(board, row, col, s_boxes, s_rows, s_cols):
            #loop to next empty spot
            while(board[row][col] != "."):
                col += 1

                if(col == 9):
                    row += 1
                    col = 0
                if(row == 9):
                    return True
        
            box_num = (row // 3) * 3 + (col // 3)

            for d in "123456789":
                #try placing it
                
                if(d in s_boxes[box_num] or d in s_rows[row] or d in s_cols[col]):
                    continue
                board[row][col] = d
                s_boxes[box_num].add(d)
                s_rows[row].add(d)
                s_cols[col].add(d)
                if(dfs(board, row, col, s_boxes, s_rows, s_cols)):
                    return True
                
                board[row][col] = "."
                s_boxes[box_num].remove(d)
                s_rows[row].remove(d)
                s_cols[col].remove(d)
            
            return False

        dfs(board, 0, 0, s_boxes, s_rows, s_cols)
        