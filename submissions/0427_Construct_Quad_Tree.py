"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def calcRange(idStart: int, idEnd: int) -> int:
            return (idEnd - idStart) // 2
        
        def isDifferent(rowStart: int, rowEnd: int, colStart: int, colEnd: int):
            idRange = calcRange(rowStart, rowEnd)
            for i in range(idRange):
                for j in range(idRange):
                    if not grid[rowStart][colStart] == grid[rowStart+i][colStart+idRange+j] == grid[rowStart+idRange+i][colStart+j] == grid[rowStart+idRange+i][colStart+idRange+j]:
                        return True
            return False
        
        def iterativeMakeTree(rowStart: int, rowEnd: int, colStart: int, colEnd: int):
            if isDifferent(rowStart, rowEnd, colStart, colEnd):
                idRange = calcRange(rowStart, rowEnd)
                currNode = Node(val=1, isLeaf=0,
                                topLeft=iterativeMakeTree(rowStart, rowStart+idRange, colStart, colStart+idRange),
                                topRight=iterativeMakeTree(rowStart, rowStart+idRange, colStart+idRange, colEnd),
                                bottomLeft=iterativeMakeTree(rowStart+idRange, rowEnd, colStart, colStart+idRange),
                                bottomRight=iterativeMakeTree(rowStart+idRange, rowEnd,  colStart+idRange, colEnd))
            else:
                currNode = Node(val=grid[rowStart][colStart], isLeaf=1,
                                topLeft=None, topRight=None, 
                                bottomLeft=None, bottomRight=None)
            return currNode

        rowStart = colStart = 0
        rowEnd = colEnd = len(grid)
        
        answer = iterativeMakeTree(rowStart, rowEnd, colStart, colEnd)
        return answer
