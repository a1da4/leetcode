class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for ch, num in zip(["a", "b", "c"], [a, b, c]):
            if num > 0:
                heapq.heappush(heap, (-num, ch))
        
        answer = []
        while heap:
            _num, ch = heapq.heappop(heap)
            num = - _num
            if len(answer) >= 2 and answer[-1] == ch and answer[-2] == ch:
                if not heap:
                    break
                _nextNum, nextCh = heapq.heappop(heap)
                answer.append(nextCh)
                if _nextNum + 1 < 0:
                    heapq.heappush(heap, (_nextNum + 1, nextCh))
                heapq.heappush(heap, (_num, ch))
            else:
                num -= 1
                answer.append(ch)
                if num > 0:
                    heapq.heappush(heap, (-num, ch))

        return "".join(answer)

