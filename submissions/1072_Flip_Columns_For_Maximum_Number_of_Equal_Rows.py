class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        booledRow2Freq = {}

        for row in matrix:
            booledRow = "".join("T" if num == row[0] else "F" for num in row)

            booledRow2Freq[booledRow] = (booledRow2Freq.get(booledRow, 0) + 1)

        return max(booledRow2Freq.values(), default=0)

