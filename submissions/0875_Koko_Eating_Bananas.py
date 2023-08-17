class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcEatTime(pile:int, k: int) -> int:
            time = 0
            time += pile // k
            time += 1 if pile % k > 0 else 0

            return time
        
        totalPiles = sum(piles)
        piles.sort()
        kMin = totalPiles // h if totalPiles >= h else 1
        kMax = piles[-1]
        while kMin < kMax:
            k = (kMin + kMax) // 2
            currTime = 0
            for pile in piles:
                currTime += pile // k
                currTime += 1 if pile % k > 0 else 0
                if currTime > h:
                    break
            if currTime <= h:
                kMax = k
            else:
                kMin = k + 1
        
        return kMin
