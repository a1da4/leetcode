class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        answer = 0
        M, N = len(picture), len(picture[0])
        rows = [0] * M
        cols = [0] * N
        for rowId in range(M):
            for colId in range(N):
                if picture[rowId][colId] == "B":
                    rows[rowId] += 1
                    cols[colId] += 1

        for rowId in range(M):
            for colId in range(N):
                if rows[rowId] == cols[colId] == 1 and picture[rowId][colId] == "B":
                    answer += 1

        return answer

