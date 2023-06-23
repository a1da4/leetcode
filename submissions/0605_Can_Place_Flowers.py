class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0
        
        countZero = 0
        addedFlowers = 0

        # consider flowerbed[0] and flowerbed[-1]
        isEdge = (flowerbed[0] == 0)
        for num in flowerbed:
            if num == 0:
                countZero += 1
            else:
                if isEdge:
                    addedFlowers += countZero // 2
                    countZero = 0
                    isEdge = False
                else:
                    addedFlowers += countZero // 3
                    if countZero > 3:
                        addedFlowers += countZero % 2
                    countZero = 0
        
        if countZero > 0:
            addedFlowers += countZero // 2
            if countZero == len(flowerbed):
                addedFlowers += countZero % 2
            countZero = 0

        return addedFlowers >= n
