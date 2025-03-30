class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch2lastId = {}
        for chId, ch in enumerate(s):
            ch2lastId[ch] = chId
        
        N = len(s)
        answer = []
        leftId = 0
        while leftId < N:
            currId = leftId
            rightId = ch2lastId[s[currId]]
            while currId < rightId:
                rightId = max(rightId, ch2lastId[s[currId]])
                currId += 1

            answer.append(rightId - leftId + 1)
            leftId = currId + 1
        return answer

