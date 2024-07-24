class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.mat = [[0] * n for _ in range(n)]
        self.finished = False
        self.winner = None

    def _verify(self, row: int, col: int, player: int) -> bool:
        if row + col == self.n - 1 or row == col:
            if all([self.mat[r][self.n - r - 1] == player for r in range(self.n)]) or \
                all([self.mat[r][r] == player for r in range(self.n)]):
                return True

        if all([self.mat[row][c] == player for c in range(self.n)]) or \
            all([self.mat[r][col] == player for r in range(self.n)]):
            return True
        return False

    def move(self, row: int, col: int, player: int) -> int:
        if self.finished:
            return self.winner
        self.mat[row][col] = player
        if self._verify(row, col, player):
            self.finished = True
            self.winner = player
            return player
        else:
            return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
