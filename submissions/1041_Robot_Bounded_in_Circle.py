class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if instructions.count("R") + instructions.count("L") == 0:
            return False

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dirId = 0
        currDir = [0, 1]
        currPos = [0, 0]

        for instruct in instructions:
            if instruct == "L":
                dirId = dirId - 1 if dirId > 0 else 3
                currDir = dirs[dirId]
            elif instruct == "R":
                dirId = (dirId + 1) % 4
                currDir = dirs[dirId]
            else:
                currPos[0] += currDir[0]
                currPos[1] += currDir[1]
        
        return currPos == [0, 0] or dirId > 0
