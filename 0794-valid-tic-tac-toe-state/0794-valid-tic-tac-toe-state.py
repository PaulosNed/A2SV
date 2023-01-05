class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        oRowCount = defaultdict(int)
        oColumnCount = defaultdict(int)
        xRowCount = defaultdict(int)
        xColumnCount = defaultdict(int)
        for i,row in enumerate(board):
            for j,letter in enumerate(row):
                if letter != " ":
                    if letter == "O":
                        oRowCount[i] += 1
                        oColumnCount[j] += 1
                    else:
                        xRowCount[i] += 1
                        xColumnCount[j] += 1
        xCount = sum(xRowCount.values())
        oCount = sum(oRowCount.values())
        if (board[0][0] == board[1][1]==board[2][2] == "O" or board[0][2] == board[1][1]==board[2][0] == "O") and xCount > oCount:
            return False
        if (board[0][0] == board[1][1]==board[2][2] == "X" or board[0][2] == board[1][1]==board[2][0] == "X") and xCount == oCount:
            return False
        if xCount == oCount or xCount - oCount == 1:
            if not xRowCount or not oRowCount:
                return True
            maxX = max(max(xRowCount.values()), max(xColumnCount.values()))
            maxO = max(max(oRowCount.values()), max(oColumnCount.values()))
            if maxX == maxO == 3:
                return False
            elif maxX == 3 and xCount == oCount:
                return False
            elif maxO == 3 and xCount > oCount:
                return False
            return True
        return False