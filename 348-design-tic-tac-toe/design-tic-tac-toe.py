class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.dia = [0]*2
        

    def move(self, row: int, col: int, player: int) -> int:
        ad = 1 if player == 1 else -1
        self.rows[row] += ad
        self.cols[col] += ad
        if row == col:
            self.dia[0] += ad
        if row + col == self.n-1:
            self.dia[1] += ad
        for i in range(self.n):
            if self.rows[i] == self.n or self.cols[i] == self.n or self.dia[0] == self.n or self.dia[1] == self.n:
                return 1
            if self.rows[i] == -self.n or self.cols[i] == -self.n or self.dia[0] == -self.n or self.dia[1] == -self.n:
                return 2
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)