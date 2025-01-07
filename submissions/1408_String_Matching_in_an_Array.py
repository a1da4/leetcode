class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        N = len(words)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if words[i] in words[j]:
                    answer.append(words[i])
                    break

        return answer

