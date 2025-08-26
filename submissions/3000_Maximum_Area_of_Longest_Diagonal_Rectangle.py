class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        answer = 0
        maxDiag = 0
        for dimension in dimensions:
            currDiag = dimension[0] ** 2 + dimension[1] ** 2
            currArea = dimension[0] * dimension[1]

            if currDiag == maxDiag:
                answer = max(answer, currArea)
            elif currDiag > maxDiag:
                maxDiag = currDiag
                answer = currArea

        return answer

