class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # perform extensive depth first search at each and every node where ever we find the string which is completely matching
        rows, cols = len(board), len(board[0])
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'v' or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = 'v'
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = temp
            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
        rows = len(board)
        cols = len(board[0])
        