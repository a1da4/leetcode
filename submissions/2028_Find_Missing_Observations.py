class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m, mSum = len(rolls), sum(rolls)
        tSum = mean * (m + n)
        if mSum + n <= tSum <= mSum + 6 * n:
            rest = tSum - mSum
            answer = [rest // n] * n
            for i in range(rest % n):
                answer[i] += 1
            return answer
        else:
            return []

