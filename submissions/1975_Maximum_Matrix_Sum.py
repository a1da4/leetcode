class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        answer = 0
        minVal = float("inf")
        negs = 0

        for row in matrix:
            for val in row:
                answer += abs(val)
                if val < 0:
                    negs += 1
                minVal = min(minVal, abs(val))

        if negs % 2 != 0:
            answer -= 2 * minVal

        return answer

