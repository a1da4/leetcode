class Solution:
    def numOfUnplacedFruits(
        self, 
        fruits: List[int],
        baskets: List[int],
    ) -> int:
        answer = 0
        filled = [False] * len(baskets)

        for fruit in fruits:
            fill = False
            for bId, basket in enumerate(baskets):
                if fruit <= basket and not filled[bId]:
                    filled[bId] = True
                    fill = True
                    break
            if not fill:
                answer += 1
        return answer
