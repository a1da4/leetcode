class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def verify(day: int) -> bool:
            currBloom = 0
            currBouquet = 0

            for bloomday in bloomDay:
                if bloomday <= day:
                    currBloom += 1
                    if currBloom == k:
                        currBouquet += 1
                        currBloom = 0
                else:
                    currBloom = 0
            
            return currBouquet >= m

        sortedDay = sorted(list(set(bloomDay)))
        answer = 0
        leftId = 0
        rightId = len(sortedDay) - 1
        while leftId <= rightId:
            midId = (leftId + rightId) // 2
            if verify(sortedDay[midId]):
                rightId = midId - 1
                answer = sortedDay[midId]
            else:
                leftId = midId + 1
        
        return answer

        
