class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        timeL = [float("inf") for _ in range(N)]
        queueL = deque([(i, 0) for i in range(N) if dominoes[i] == "L"])
        visitedL = set()
        while queueL:
            n = len(queueL)
            for _ in range(n):
                domino, time = queueL.popleft()
                visitedL.add(domino)
                timeL[domino] = time
                nextDomino = domino - 1
                if (
                    0 <= nextDomino < N
                    and nextDomino not in visitedL
                    and dominoes[nextDomino] == "."
                ):
                    queueL.append((nextDomino, time + 1))

        timeR = [float("inf") for _ in range(N)]
        queueR = deque([(i, 0) for i in range(N) if dominoes[i] == "R"])
        visitedR = set()
        while queueR:
            n = len(queueR)
            for _ in range(n):
                domino, time = queueR.popleft()
                visitedR.add(domino)
                timeR[domino] = time
                nextDomino = domino + 1
                if (
                    0 <= nextDomino < N
                    and nextDomino not in visitedR
                    and dominoes[nextDomino] == "."
                ):
                    queueR.append((nextDomino, time + 1))

        answer = ["" for _ in range(N)]
        for i in range(N):
            if dominoes[i] != ".":
                answer[i] = dominoes[i]
            else:
                if timeL[i] < timeR[i]:
                    answer[i] = "L"
                elif timeL[i] > timeR[i]:
                    answer[i] = "R"
                else:
                    answer[i] = "."

        return "".join(answer)

