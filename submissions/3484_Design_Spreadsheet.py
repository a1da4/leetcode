class Spreadsheet:
    def __init__(self, rows: int):
        self.mat = [[0 for _ in range(rows)] for _ in range(26)]

    def getId(self, cell: str) -> Tuple[int]:
        row, col = cell[0], cell[1:]
        rowId = ord(row) - ord("A")
        colId = int(col) - 1
        return rowId, colId
    
    def getNum(self, string: str) -> int:
        if ord("A") <= ord(string[0]) <= ord("Z"):
            rowId, colId = self.getId(string)
            return self.mat[rowId][colId]
        else:
            return int(string)

    def setCell(self, cell: str, value: int) -> None:
        rowId, colId = self.getId(cell)
        self.mat[rowId][colId] = value

    def resetCell(self, cell: str) -> None:
        rowId, colId = self.getId(cell)
        self.mat[rowId][colId] = 0

    def getValue(self, formula: str) -> int:
        total = 0
        curr = ""
        for ch in formula[1:]:
            if ch == "+":
                total += self.getNum(curr)
                curr = ""
            else:
                curr += ch
            
        if curr != "":
            total += self.getNum(curr)

        return total

