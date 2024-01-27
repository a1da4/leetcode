class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        prevRow = [1]
        for _ in range(numRows - 1):
            currRow = [1]
            if len(prevRow) > 1:
                currRow = currRow + [leftNum + rightNum for leftNum, rightNum in zip(prevRow[:-1], prevRow[1:])]
            currRow.append(1)
            answer.append(currRow)
            prevRow = currRow
        return answer
