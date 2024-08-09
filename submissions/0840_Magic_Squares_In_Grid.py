class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def verify(mat) -> bool:
            nums = set()
            for row in mat:
                for num in row:
                    if num == 0 or num >= 10 or num in nums:
                        return False
                    nums.add(num)

            return sum(mat[0]) == sum(mat[1]) == sum(mat[2]) == \
                    sum([row[0] for row in mat]) == \
                    sum([row[1] for row in mat]) == \
                    sum([row[2] for row in mat]) == \
                    mat[0][0] + mat[1][1] + mat[2][2] == \
                    mat[0][2] + mat[1][1] + mat[2][0]
        
        answer = 0

        numRow, numCol = len(grid), len(grid[0])
        for row in range(numRow - 2):
            for col in range(numCol - 2):
                mat = [grid[r][col:col+3] for r in range(row, row+3)]
                if verify(mat):
                    answer += 1

        return answer

