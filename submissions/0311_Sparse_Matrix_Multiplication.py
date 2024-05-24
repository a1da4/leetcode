class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        numRow = len(mat1)
        numCol = len(mat2[0])
        numMid = len(mat1[0])
        answer = [[0] * numCol for _ in range(numRow)]

        for colId in range(numCol):
            for rowId in range(numRow):
                answer[rowId][colId] = sum([mat2[_midId][colId] * mat1[rowId][_midId] \
                                            for _midId in range(numMid)])

        return answer

