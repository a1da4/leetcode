class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for row in range(len(matrix)):
            matrix[row].append("0")

        height = [0] * len(matrix[0])
        maxRec = 0

        for row in matrix:
            stack = [-1]
            for colId, val in enumerate(row):
                height[colId] = (height[colId] + 1) * int(val)
                while height[stack[-1]] > height[colId]:
                    colIdPrev = stack.pop()
                    leftId = colIdPrev - stack[-1] - 1
                    rightId = colId - colIdPrev

                    maxRec = max(maxRec, (leftId + rightId) * height[colIdPrev])

                stack.append(colId)

        return maxRec
