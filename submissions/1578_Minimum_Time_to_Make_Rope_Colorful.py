class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # find substring (same color)
        # find max time
        # needed time = sum - max
        numBalloon = len(colors)
        totalCost = 0
        currId = 0
        while currId < numBalloon:
            currColor = colors[currId]
            sameIds = [currId]
            currId += 1
            while currId < numBalloon:
                if currColor == colors[currId]:
                    sameIds.append(currId)
                    currId += 1
                else:
                    break
            if len(sameIds) > 1:
                times = [neededTime[sameId] for sameId in sameIds]
                totalCost += sum(times) - max(times)
        return totalCost
