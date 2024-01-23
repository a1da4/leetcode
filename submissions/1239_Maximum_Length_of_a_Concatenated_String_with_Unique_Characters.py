class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = [""]
        answer = 0
        for word in arr:
            N = len(results)
            for currId in range(N):
                newResult = results[currId] + word
                newL = len(newResult)
                if newL != len(set(newResult)):
                    continue
                results.append(newResult)
                answer = max(answer, newL)
        return answer
