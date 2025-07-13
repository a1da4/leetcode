class Solution:
    def matchPlayersAndTrainers(
        self, 
        players: List[int], 
        trainers: List[int],
    ) -> int:
        players.sort()
        trainers.sort()

        answer = 0
        tId = 0
        n = len(trainers)
        for player in players:
            while tId < n and player > trainers[tId]:
                tId += 1
            if tId >= n:
                break
            
            if player <= trainers[tId]:
                answer += 1
                tId += 1

        return answer
