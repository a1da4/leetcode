class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        answer = []
        queue = deque([(n, 2, [])])

        while queue:
            num, start, factors = queue.popleft()
            for factor in range(start, int(num ** 0.5) + 1):
                if num % factor == 0:
                    new_factors = factors + [factor]
                    answer.append(new_factors + [num // factor])
                    queue.append((num // factor, factor, new_factors))

        return answer


