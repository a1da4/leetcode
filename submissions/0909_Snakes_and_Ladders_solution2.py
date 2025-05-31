class Solution:
    def snakesAndLadders(
        self, 
        board: List[List[int]],
    ) -> int:
        n = len(board)

        def detect_position(
            num: int,
        ) -> Tuple[int]:
            r = n - num // n
            if num % n > 0:
                r -= 1

            remain = num - (n - 1 - r) * n
            if (n - 1) % 2 == r % 2:
                c = remain - 1
            else:
                c = n - remain

            return r, c

        queue = deque([1])
        goal = n * n
        visited = [False] * (goal + 1)
        visited[1] = True
        answer = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                num = queue.popleft()  
                if num == goal:
                    return answer

                for d in range(1, 7):
                    _num = num + d
                    if _num > goal:
                        continue

                    _r, _c = detect_position(_num)
                    if board[_r][_c] > 0:
                        _num = board[_r][_c]

                    if visited[_num]:
                        continue
                    queue.append(_num)
                    visited[_num] = True
            answer += 1

        return -1

