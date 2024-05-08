class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted([[athlete, score[athlete]] for athlete in range(len(score))], \
                            key=lambda x:x[1], reverse=True)

        answer = [""] * len(sortedScore)
        for rank in range(len(sortedScore)):
            athlete, score = sortedScore[rank]
            if rank == 0:
                answer[athlete] = 'Gold Medal'
            elif rank == 1:
                answer[athlete] = 'Silver Medal'
            elif rank == 2:
                answer[athlete] = 'Bronze Medal'
            else:
                answer[athlete] = str(rank + 1) 

        return answer

