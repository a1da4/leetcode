class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        answer = 0
        N = len(arr)

        dp = [[0] * N for _ in range(N)]
        num2id = {num: i for i, num in enumerate(arr)}

        for currId in range(N):
            for prevId in range(currId):
                diff = arr[currId] - arr[prevId]
                pastId = num2id[diff] if diff in num2id else -1

                dp[prevId][currId] = (
                    dp[pastId][prevId] + 1
                    if diff < arr[prevId] and pastId >= 0
                    else 2
                )
                answer = max(answer, dp[prevId][currId])

        return answer if answer > 2 else 0

