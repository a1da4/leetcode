class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        answer = 0
        for rowId in range(len(picture)):
            for colId in range(len(picture[0])):
                if picture[rowId][colId] == "B":
                    cols = [1 if picture[rowId][_colId] == "B" else 0 for _colId in range(len(picture[0]))]
                    rows = [1 if picture[_rowId][colId] == "B" else 0 for _rowId in range(len(picture))]
                    if sum(cols) + sum(rows) == 2:
                        answer += 1
        return answer
