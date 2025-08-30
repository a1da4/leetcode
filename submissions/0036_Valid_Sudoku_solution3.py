class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # col
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in nums:
                    return False
                else:
                    nums.add(board[row][col])
        # row
        for row in range(9):
            nums = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in nums:
                    return False
                else:
                    nums.add(board[row][col])
        
        # matrix
        for rId in range(3):
            for cId in range(3):
                left = rId * 3
                right = left + 3
                up = cId * 3
                down = up + 3
                nums = set()
                for row in range(left, right):
                    for col in range(up, down):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] in nums:
                            return False
                        else:
                            nums.add(board[row][col])

        return True
