class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_unique(values):
            vals = []
            for i in range(len(values)):
                if values[i] == '.':
                    continue
                elif values[i] not in vals:
                    vals.append(values[i])
                elif values[i] in vals:
                    return False
            return True

        def check_square(board):
            for i in range(0,len(board),3):
                vals = board[i:i+3]
                box1 = []
                box2 = []
                box3 = []
            
                for j in vals:
                    box1.extend(j[0:3])
                    box2.extend(j[3:6])
                    box3.extend(j[6:])
                box1_val = is_unique(box1)
                box2_val = is_unique(box2)
                box3_val = is_unique(box3)
                if not (box1_val and box2_val and box3_val):
                    return False
            return True

        def check_row(board):
            for i in range(0,len(board)):
                val = is_unique(board[i])
                if not val:
                    return False
            return True

        def check_col(board):
            for i in range(len(board)):
                values = []
                for j in range(len(board)):
                    values.append(board[j][i])
                val = is_unique(values)
                if not val:
                    return False
            return True
        return (check_square(board) and check_col(board) and check_row(board))
