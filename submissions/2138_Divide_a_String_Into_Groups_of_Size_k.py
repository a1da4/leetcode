class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        N = len(s)
        answer = []
        for i in range(N // k + 1):
            currId = i * k
            if currId >= N:
                break
            curr = s[currId:currId + k]
            n = len(curr)
            if n < k:
                curr += fill * (k - n)
            answer.append(curr)

        return answer
