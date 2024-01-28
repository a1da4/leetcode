class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        answer = 0
        numRow = len(matrix)
        numCol = len(matrix[0])

        for rowId in range(numRow):
            for colId in range(1, numCol):
                matrix[rowId][colId] += matrix[rowId][colId - 1]
        for colId in range(numCol):
            for rowId in range(1, numRow):
                matrix[rowId][colId] += matrix[rowId - 1][colId]

        for x1 in range(numRow):
            for x2 in range(x1, numRow):
                sum2freq = defaultdict(int)
                sum2freq[0] = 1
                for y in range(numCol):
                    currSum = matrix[x2][y] - matrix[x1][y] if x1 < x2 else matrix[x1][y]
                    answer += sum2freq[currSum - target]
                    sum2freq[currSum] += 1

        return answer
