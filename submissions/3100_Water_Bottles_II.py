class Solution:
    def maxBottlesDrunk(
        self, 
        numBottles: int, 
        numExchange: int,
    ) -> int:
        answer = 0
        numEmpty = 0
        while numBottles > 0:
            answer += numBottles
            numEmpty += numBottles
            numBottles = 0
            while numEmpty >= numExchange:
                numBottles += 1
                numEmpty -= numExchange
                numExchange += 1

        return answer
        
