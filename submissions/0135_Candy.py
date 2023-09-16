class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for currChild in range(1, len(ratings)):
            if ratings[currChild - 1] < ratings[currChild]:
                candies[currChild] = candies[currChild - 1] + 1
        
        for currChild in range(len(ratings)-2, -1, -1):
            if ratings[currChild] > ratings[currChild + 1]:
                candies[currChild] = max(candies[currChild], candies[currChild + 1] + 1)

        return sum(candies)
