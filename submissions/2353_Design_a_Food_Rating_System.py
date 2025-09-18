class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food2cuisine = {}
        self.food2rating = {}
        self.cuisine2heap = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food2cuisine[food] = cuisine
            self.food2rating[food] = rating
            heapq.heappush(self.cuisine2heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        self.food2rating[food] = newRating
        cuisine = self.food2cuisine[food]
        heapq.heappush(self.cuisine2heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine2heap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food2rating[food]:
                return food
            heapq.heappop(heap)

