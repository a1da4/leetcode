class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        tId = tIdPrev = 0
        while tId < len(target):
            count += 1
            for sChar in source:
                if sChar == target[tId]:
                    tId += 1
                    if tId == len(target):
                        return count
            if tId == tIdPrev:
                return -1
            tIdPrev = tId

        return count
