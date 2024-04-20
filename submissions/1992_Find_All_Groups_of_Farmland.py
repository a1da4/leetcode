class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def search(rowId: int, colId: int, rc: List[int]):
            if rowId < 0 or rowId >= len(land):
                return rc
            if colId < 0 or colId >= len(land[0]):
                return rc
            
            if land[rowId][colId] in [1, "_"]:
                land[rowId][colId] = "_"
                if rowId + 1 < len(land) and land[rowId + 1][colId]:
                    return search(rowId + 1, colId, [rc[0] + 1, rc[1]])
                elif colId + 1 < len(land[0]) and land[rowId][colId + 1]:
                    return search(rowId, colId + 1, [rc[0], rc[1] + 1])
                else:
                    return rc
            else:
                return rc
        
        def delete(rowId: int, colId: int, rc: List[int]):
            for _rowId in range(rowId, rc[0] + 1):
                for _colId in range(colId, rc[1] + 1):
                    land[_rowId][_colId] = "_"
            
        answer = []
        for rowId in range(len(land)):
            for colId in range(len(land[0])):
                if land[rowId][colId] == 1:
                    rc = search(rowId, colId, [rowId, colId])
                    answer.append([rowId, colId] + rc)
                    delete(rowId, colId, rc)

        return answer

