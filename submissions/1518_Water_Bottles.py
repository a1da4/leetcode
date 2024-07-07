class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        emptyBottles = 0

        while numBottles > 0:
            answer += numBottles
            emptyBottles += numBottles
            numBottles = int(emptyBottles // numExchange)
            emptyBottles = emptyBottles % numExchange

        return answer

