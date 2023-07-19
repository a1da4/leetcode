class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)

        rQueue = deque()
        dQueue = deque()

        for currId, currSenate in enumerate(senate):
            if currSenate == "R":
                rQueue.append(currId)
            else:
                dQueue.append(currId)

        while rQueue and dQueue:
            rTurn = rQueue.popleft()
            dTurn = dQueue.popleft()

            if rTurn < dTurn:
                rQueue.append(rTurn + N)
            else:
                dQueue.append(dTurn + N)
        
        if rQueue:
            return "Radiant"
        else:
            return "Dire"
