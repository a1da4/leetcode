class Leaderboard:

    def __init__(self):
        self.playerId2score = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.playerId2score[playerId] += score

    def top(self, K: int) -> int:
        return sum([score for (pId, score) \
                    in self.playerId2score.most_common(K)])

    def reset(self, playerId: int) -> None:
        self.playerId2score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
