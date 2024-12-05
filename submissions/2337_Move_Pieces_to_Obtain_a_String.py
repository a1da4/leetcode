class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sQueue = deque([])
        tQueue = deque([])

        for i in range(len(start)):
            if start[i] != "_":
                sQueue.append((start[i], i))
            if target[i] != "_":
                tQueue.append((target[i], i))

        if len(sQueue) != len(tQueue):
            return False

        while sQueue:
            sChar, sId = sQueue.popleft()
            tChar, tId = tQueue.popleft()
            if sChar != tChar or (sChar == "L" and sId < tId) or (tChar == "R" and sId > tId):
                return False
        return True

