class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        INF = float("inf")
        N = len(dominoes)

        timeL = [INF] * N
        time = INF
        for i, ch in enumerate(dominoes):
            if ch == 'R':
                time = 0
            elif ch == 'L':
                time = INF
            else:
                if time < INF:
                    time += 1
            timeL[i] = time
        
        timeR = [INF] * N
        time = INF
        for i in range(N - 1, -1, -1):
            ch = dominoes[i]
            if ch == 'L':
                time = 0
            elif ch == 'R':
                time = INF
            else:
                if time < INF:
                    time += 1
            timeR[i] = time

        answer = ["" for _ in range(N)]
        for i in range(N):
            if dominoes[i] != ".":
                answer[i] = dominoes[i]
            else:
                if timeL[i] == timeR[i]:
                    answer[i] = "."
                elif timeL[i] > timeR[i]:
                    answer[i] = "L"
                else:
                    answer[i] = "R"

        return "".join(answer)

