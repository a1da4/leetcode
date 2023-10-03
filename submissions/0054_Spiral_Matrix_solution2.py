class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.answer = []
        self.currItems = 0
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])

        self.iters = 0
        self.currPosition = [0, 0]

        def update(currNum: int):
            self.answer.append(currNum)
            self.currItems += 1

        def goRight(matrix: List[List[int]]):
            currRow = self.currPosition[0]
            for currCol in range(self.iters, self.numCols - self.iters):
                update(matrix[currRow][currCol])
            self.currPosition[1] = self.numCols - self.iters - 1
        
        def goLeft(matrix: List[List[int]]):
            currRow = self.currPosition[0]
            for currCol in range(self.numCols - self.iters - 1, self.iters - 1, -1):
                update(matrix[currRow][currCol])
            self.currPosition[1] = self.iters
        
        def goDown(matrix: List[List[int]]):
            currCol = self.currPosition[1]
            for currRow in range((self.iters + 1), self.numRows - (self.iters + 1)):
                update(matrix[currRow][currCol])
            self.currPosition[0] = self.numRows - self.iters - 1
        
        def goUp(matrix: List[List[int]]):
            currCol = self.currPosition[1]
            for currRow in range(self.numRows - (self.iters + 1) - 1, self.iters, -1):
                update(matrix[currRow][currCol])
            self.currPosition[0] = self.iters + 1
        
        def isFull():
            return self.currItems == self.numRows * self.numCols

        while self.currItems < self.numRows * self.numCols:
            goRight(matrix)
            if isFull():
                continue
            goDown(matrix)
            if isFull():
                continue
            goLeft(matrix)
            if isFull():
                continue
            goUp(matrix)
            self.iters += 1

        return self.answer
