class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        answer = 0

        points.sort(key=lambda t: (t[0], -t[1]))

        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                a, b = points[i], points[j]
                if a[1] < b[1]:
                    continue
                verified = 1
                for k in range(i + 1, j):
                    c = points[k]
                    if a[1] >= c[1] >= b[1]:
                        verified = 0
                        break

                answer += verified 

        return answer
