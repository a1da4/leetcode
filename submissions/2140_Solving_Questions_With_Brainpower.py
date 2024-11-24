class Solution:
    def _travel(self, 
                currId: int, 
                questions: List[List[int]]) -> int:
        if currId >= len(questions):
            return 0
        elif currId not in self.memo:
            point, brain = questions[currId]
            self.memo[currId] = max(point + self._travel(currId + brain + 1,
                                                         questions), 
                                    self._travel(currId + 1, questions))
        else:
            pass
        
        return self.memo[currId]

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.memo: Dict[int, int] = {}

        return self._travel(0, questions)

