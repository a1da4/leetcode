class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer = 0
        N = len(rating)
        
        incrTeams = [[0] * 4 for _ in range(N)]
        decrTeams = [[0] * 4 for _ in range(N)]

        for i in range(N):
            incrTeams[i][1] = 1
            decrTeams[i][1] = 1

        for count in range(2, 4):
            for i in range(N):
                for j in range(i + 1, N):
                    if rating[i] < rating[j]:
                        incrTeams[j][count] += incrTeams[i][count - 1]
                    if rating[i] > rating[j]:
                        decrTeams[j][count] += decrTeams[i][count - 1]

        for i in range(N):
            answer += incrTeams[i][3] + decrTeams[i][3]

        return answer
