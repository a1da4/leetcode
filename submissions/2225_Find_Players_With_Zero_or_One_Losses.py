class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerC = Counter([match[0] for match in matches])
        loserC = Counter([match[1] for match in matches])
        
        loserVocab = set(loserC.keys())

        answer0 = []
        for winner in sorted(winnerC.keys()):
            if winner in loserVocab:
                continue
            answer0.append(winner)

        answer1 = []
        for loser in sorted(loserC.keys()):
            if loserC[loser] == 1:
                answer1.append(loser)
        
        return [answer0, answer1]
