class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:   
        numRow, numCol = len(maze), len(maze[0])
        dirs = ((1,0), (-1,0), (0,1), (0,-1))

        startRow, startCol = entrance
        maze[startRow][startCol] = "+"

        queue = deque()
        queue.append([startRow, startCol, 0])

        while queue:
            currRow, currCol, currDist = queue.popleft()

            for d in dirs:
                nextRow = currRow + d[0]
                nextCol = currCol + d[1]

                if 0 <= nextRow < numRow and 0 <= nextCol < numCol and maze[nextRow][nextCol] == ".":

                    if 0 == nextRow or nextRow == numRow - 1 or 0 == nextCol or nextCol == numCol - 1:
                        return currDist + 1
                    
                    maze[nextRow][nextCol] = "+"
                    queue.append([nextRow, nextCol, currDist + 1])
        
        return -1
