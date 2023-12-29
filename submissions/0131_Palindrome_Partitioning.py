class Solution:
    def partition(self, s: str) -> List[List[str]]:
        numString = len(s)
        answer = []
        if numString == 0:
            return [[]]
        for splitId in range(1, numString + 1):
            if s[:splitId] != s[:splitId][::-1]:
                continue
            restSplits = self.partition(s[splitId:])
            for rest in restSplits:
                answer.append([s[:splitId]] + rest)
        return answer
