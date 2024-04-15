class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def verify(moves: List[List[int]]) -> bool:
            diag_1 = [[0,0], [1,1], [2,2]]
            diag_2 = [[0,2], [1,1], [2,0]]

            return Counter([move[0] for move in moves]).most_common()[0][1] == 3 or \
                Counter([move[1] for move in moves]).most_common()[0][1] == 3 or \
                all([diag in moves for diag in diag_1]) or \
                all([diag in moves for diag in diag_2])

        if verify(moves):
            moves = deque(moves)
            a_moves = []
            b_moves = []
            while moves:
                xa_move = moves.popleft()
                a_moves.append(xa_move)
                if moves:
                    ob_move = moves.popleft()
                    b_moves.append(ob_move)

            if verify(a_moves):
                return "A"
            elif verify(b_moves):
                return "B"
            elif len(a_moves) + len(b_moves) < 9:
                return "Pending"
            else:
                return "Draw"
        else:
            return "Pending"
