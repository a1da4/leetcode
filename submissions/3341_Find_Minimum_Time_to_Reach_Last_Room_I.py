class Solution:
    def minTimeToReach(
        self, 
        moveTime: List[List[int]],
    ) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [
            [1, 0], [-1, 0],
            [0, 1], [0, -1],
        ]
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        arriveTime = [
            [float('inf') for _ in range(m)] 
            for _ in range(n)
        ]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == n - 1 and c == m - 1:
                return time

            for direction in directions:
                _r = r + direction[0]
                _c = c + direction[1]

                if (0 <= _r < n and
                    0 <= _c < m):
                    _time = max(
                        moveTime[_r][_c],
                        time,
                    ) + 1

                    if _time < arriveTime[_r][_c]:
                        arriveTime[_r][_c] = _time
                        heapq.heappush(
                            heap,
                            (_time, _r, _c),
                        )

        return -1

