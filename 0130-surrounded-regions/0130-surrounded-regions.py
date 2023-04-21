class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        def dfs(r, c, val):
            directions = [(0,-1), (0,1), (-1,0), (1,0)]
            stack = [(r,c)]
            while stack:
                cr, cc = stack.pop()
                if 0 <= cr < len(board) and 0 <= cc < len(board[0]) and board[cr][cc] == 'O':
                    board[cr][cc] = val
                    
                    for direction in directions:
                        stack.append(((cr  + direction[0]), (cc  + direction[1])))
        
        
        border = [0, len(board)-1]
        borderCol = [0, len(board[0])-1]
        
        for r in border:
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    dfs(r, c, 'P')
        
        for c in borderCol:
            for r in range(len(board)):
                if board[r][c] == 'O':
                    dfs(r, c, 'P')
                    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    dfs(r, c, 'X')
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'P':
                    board[r][c] = 'O'
        
        
        
                