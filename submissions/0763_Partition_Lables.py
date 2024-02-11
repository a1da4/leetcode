class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        char2lastId = {s[lastId]: lastId for lastId in range(N)}
        currId = 0
        answer = []
        while currId < N:
            lastId = char2lastId[s[currId]]
            nextId = currId + 1
            while nextId < lastId:
                if char2lastId[s[nextId]] > lastId:
                    lastId = char2lastId[s[nextId]]
                nextId += 1
            
            answer.append(lastId - currId + 1)
            currId = lastId + 1

        return answer
