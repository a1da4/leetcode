class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def goRight(matrix: List[List[int]], threshRight: int):
            threshLeft = self.iters 
            if threshLeft < threshRight:
                for currCol in range(threshLeft, threshRight):
                    currNum = matrix[self.currPosition[0]][currCol]
                    self.answer.append(currNum)
                    self.currItems += 1
                self.currPosition[1] = threshRight - 1
            else:
                currNum = matrix[self.currPosition[0]][threshLeft - 1]
                self.answer.append(currNum)
                self.currItems += 1

        def goDown(matrix: List[List[int]], threshDown: int):
            threshUp = self.currPosition[0] + 1
            if threshUp < threshDown:
                for currRow in range(threshUp, threshDown):
                    currNum = matrix[currRow][self.currPosition[1]]
                    self.answer.append(currNum)
                    self.currItems += 1
                self.currPosition[0] = threshDown - 1
            else:
                currNum = matrix[threshUp - 1][self.currPosition[1]]
                self.answer.append(currNum)
                self.currItems += 1
        
        def goLeft(matrix: List[List[int]], threshLeft: int):
            threshRight = self.currPosition[1] - 1
            if threshRight > threshLeft - 1:
                for currCol in range(threshRight, threshLeft - 1, -1):
                    currNum = matrix[self.currPosition[0]][currCol]
                    self.answer.append(currNum)
                    self.currItems += 1
                self.currPosition[1] = threshLeft
            else:
                currNum = matrix[self.currPosition[0]][threshRight]
                self.answer.append(currNum)
                self.currItems += 1

        def goUp(matrix: List[List[int]], threshUp: int):
            threshDown = self.currPosition[0] - 1
            if threshDown > threshUp:
                for currRow in range(threshDown, threshUp, -1):
                    currNum = matrix[currRow][self.currPosition[1]]
                    self.answer.append(currNum)
                    self.currItems += 1
                self.currPosition[0] = threshUp + 1
            else:
                currNum = matrix[threshDown][self.currPosition[1]]
                self.answer.append(currNum)
                self.currItems += 1

        self.answer = []
        self.currItems = 0
        numRows = len(matrix)
        numCols = len(matrix[0])

        self.iters = 0
        self.currPosition = [0, 0]
        while self.currItems < numRows * numCols:
            goRight(matrix, numCols - self.iters)
            if self.currItems == numRows * numCols:
                continue
            goDown(matrix, numRows - self.iters)
            if self.currItems == numRows * numCols:
                continue
            goLeft(matrix, self.iters)
            if self.currItems == numRows * numCols:
                continue
            goUp(matrix, self.iters)
            self.iters += 1

        return self.answer
