class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        totalProfit = 0
        currProfit = 0
        startStation = 0

        for currStation in range(len(gas)):
            currGas = gas[currStation] - cost[currStation]
            totalProfit += currGas
            currProfit += currGas
            if currProfit < 0:
                currProfit = 0
                startStation = currStation + 1
        
        if totalProfit < 0:
            return -1
        else:
            return startStation
