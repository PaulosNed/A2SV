class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in columns[j]:
                        return False
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
        rs = 0
        cs = 0
        while (rs+2 < len(board)):
            cs = 0
            while(cs+2 < len(board[0])):
                checker = set()
                for r in range(rs,rs+3):
                    for c in range(cs, cs+3):
                        if board[r][c].isdigit():
                            if board[r][c] in checker:
                                return False
                            checker.add(board[r][c])
                cs += 3
            rs += 3
        return True