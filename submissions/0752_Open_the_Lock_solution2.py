class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        pathes = [("0000", 0)]

        def move(target: str):
            moved = []
            for i in range(4):
                digit = int(target[i])
                for sign in (-1, 1):
                    nextDigit = (digit + sign) % 10
                    moved.append(target[:i] + str(nextDigit) + target[i+1:])
            return moved

        while pathes:
            N = len(pathes)
            for _ in range(N):
                path, numMove = pathes.pop(0)
                if path == target:
                    return numMove
                for nextPath in move(path):
                    if nextPath not in visited:
                        pathes.append((nextPath, numMove + 1))
                        visited.add(nextPath)

        return -1

