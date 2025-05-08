class Solution:
    def minTimeToReach(
        self, 
        moveTime: List[List[int]],
    ) -> int:

        n, m = len(moveTime), len(moveTime[0])
        arriveTime = [
            [float('inf') for _ in range(m)]
            for _ in range(n)
        ]
        heap = []
        heapq.heappush(
            heap,
            (0, 0, 0, 1),
        )

        while heap:
            time, r, c, i = heapq.heappop(heap)

            if r == n - 1 and c == m - 1:
                return time
            
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                _r, _c = r + d[0], c + d[1]
                if (0 > _r
                    or _r >= n
                    or 0 > _c
                    or _c >= m):
                    continue
                
                _time = max(
                    moveTime[_r][_c],
                    time,
                )
                _time += 1 if i % 2 else 2
                if _time < arriveTime[_r][_c]:
                    arriveTime[_r][_c] = _time
                    heapq.heappush(
                        heap,
                        (_time, _r, _c, i + 1),
                    )
        
        return -1
