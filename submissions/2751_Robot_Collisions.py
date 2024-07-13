class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)
        ids = list(range(N))
        stack = deque([])

        ids.sort(key=lambda x: positions[x])

        for currId in ids:
            if directions[currId] == 'R':
                stack.append(currId)
            else:
                while stack and healths[currId] > 0:
                    topId = stack.pop()
                    if healths[topId] > healths[currId]:
                        healths[topId] -= 1
                        healths[currId] = 0
                        stack.append(topId)
                    elif healths[topId] < healths[currId]:
                        healths[currId] -= 1
                        healths[topId] = 0
                    else:
                        healths[currId] = 0
                        healths[topId] = 0

        result = []
        for currId in range(N):
            if healths[currId] > 0:
                result.append(healths[currId])
        
        return result
