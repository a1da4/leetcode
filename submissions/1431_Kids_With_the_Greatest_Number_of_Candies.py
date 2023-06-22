class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandiesNum = max(candies)
        maxCandiesIndex = candies.index(maxCandiesNum)
        
        numKids = len(candies)
        answer = []
        for currentKid in range(numKids):
            if currentKid == maxCandiesIndex:
                answer.append(True)
            else:
                currentCandiesNum = candies[currentKid] + extraCandies
                answer.append(currentCandiesNum >= maxCandiesNum)

        return answer
