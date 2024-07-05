class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # knight can move (+-1, +-2), (+-2, +-1)
        # store visited: set[Tuple[int]]
        visited = set()
        visited.add((0, 0))
        queue = deque([(0, 0)])
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                 (2, 1), (2, -1), (-2, 1), (-2, -1)]
        turn = 0
        while queue:
            N = len(queue)
            for _ in range(N):
                pos = queue.popleft()
                if pos[0] == x and pos[1] == y:
                    return turn
                for move in moves:
                    _x, _y = pos[0] + move[0], pos[1] + move[1]
                    if (_x, _y) not in visited:
                        queue.append((_x, _y))
                        visited.add((_x, _y))
            turn += 1
