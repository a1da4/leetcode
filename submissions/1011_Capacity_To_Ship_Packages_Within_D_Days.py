class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capacity: max(weights) <= capacity <= sum(weights)
        # binary search mean(maxCap, minCap)
        ## if ship_until_days -> currentCap = mean(currentCap, minCap)
        ## else -> currentCap = mean(maxCap, currentCap)

        minCap = max(weights)
        maxCap = sum(weights)
        currentCap = (minCap + maxCap) // 2

        def packing(currentCap: int, weights: List[int]) -> int:
            day = 1
            currentWeight = 0
            for weight in weights:
                if currentWeight + weight <= currentCap:
                    currentWeight += weight
                else:
                    # reset, day++
                    currentWeight = weight
                    day += 1
            return day

        def update(currentCap: int, minCap: int, maxCap: int, takeDays: int, days: int) -> Tuple[int]:
            temp = currentCap
            if takeDays <= days:
                # smaller capacity
                currentCap = (currentCap + minCap) // 2
                maxCap = temp
            else:
                # bigger capacity
                currentCap = (currentCap + maxCap) // 2
                # minCap: bigger capacity than temp(currentCap) 
                minCap = temp + 1
            return currentCap, minCap, maxCap

        while minCap < maxCap:
            takeDays = packing(currentCap, weights)
            currentCap, minCap, maxCap = update(currentCap, minCap, maxCap, takeDays, days)
        
        return minCap
