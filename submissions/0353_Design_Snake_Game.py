class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.isOver = False
        self.score = 0
        self.visited = deque([])
        self.dir2move = {"L": (0, -1), "R": (0, 1),
                         "U": (-1, 0), "D": (1, 0)}
        self.pos = [0, 0]
        self.foods = food
        self.mat = [[0] * width for _ in range(height)]

    def move(self, direction: str) -> int:
        if self.isOver:
            return -1
        
        dx, dy = self.dir2move[direction]
        self.pos[0] += dx
        self.pos[1] += dy
        
        if self.pos[0] < 0 or self.pos[0] >= len(self.mat) or \
            self.pos[1] < 0 or self.pos[1] >= len(self.mat[0]):
            self.isOver = True
            return -1
        
        if (self.pos[0], self.pos[1]) in self.visited:
            self.isOver = True
            return -1

        self.visited.append((self.pos[0], self.pos[1]))
        
        if self.foods:
            if self.pos[0] == self.foods[0][0] and \
                self.pos[1] == self.foods[0][1]:
                self.foods.pop(0)
                self.score += 1

        while len(self.visited) > self.score:
            self.visited.popleft()

        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
