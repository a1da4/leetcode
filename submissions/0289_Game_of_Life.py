class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def obtain_neighbors(i: int, j: int, mat: List[List[int]]) -> List[List[int]]:
            return [mat[i+di][j+dj] \
                    for di in range(-1, 2) \
                    for dj in range(-1, 2) \
                    if 0<=i+di<len(mat) \
                        and 0<=j+dj<len(mat[0]) 
                        and not (di==0 and dj==0)]
        
        def classify(val: int, neighbors: List[List[int]]) -> bool:
            neighborsSum = sum(neighbors)
            if val == 1 and 2 <= neighborsSum <= 3:
                return True
            elif val == 0 and neighborsSum == 3:
                return True
            else:
                return False

        #TODO _board -> changedIds
        _board = copy.deepcopy(board)
        for currRow in range(len(_board)):
            for currCol in range(len(_board[0])):
                neighbors = obtain_neighbors(currRow, 
                                             currCol,
                                             _board)
                if classify(_board[currRow][currCol], 
                            neighbors):
                    board[currRow][currCol] = 1
                else:
                    board[currRow][currCol] = 0
