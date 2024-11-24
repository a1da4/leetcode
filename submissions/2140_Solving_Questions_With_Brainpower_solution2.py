class Solution:
    def _travel(self, 
                currId: int, 
                questions: List[List[int]]) -> int:
        if currId >= self.N:
            return 0
        elif self.dp[currId] == 0:
            point, brain = questions[currId]
            self.dp[currId] = max(point + self._travel(currId + brain + 1,
                                                       questions), 
                                  self._travel(currId + 1, questions))
        else:
            pass
        
        return self.dp[currId]

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.N = len(questions)
        self.dp: List[int] = [0] * self.N

        return self._travel(0, questions)

