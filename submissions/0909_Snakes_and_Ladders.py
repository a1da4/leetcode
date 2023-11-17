class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def find_i_in_mat(i: int) -> int:
            quotient = (i - 1)//n
            remainder = (i - 1)%n
            row_id = (n - 1) - quotient
            col_id = remainder if quotient%2 == 0 else (n - 1) - remainder
            return board[row_id][col_id]

        queue = deque()
        queue.append([1, 0])
        visited = set()

        while queue:
            curr_cell, curr_moves = queue.popleft()
            curr_val = find_i_in_mat(curr_cell)
            if curr_val != -1:
                curr_cell = curr_val
            if curr_cell == n*n:
                return curr_moves
            
            for next_move in range(1, 7):
                next_cell = curr_cell + next_move
                if next_cell > n*n:
                    continue
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, curr_moves + 1))

        return -1

