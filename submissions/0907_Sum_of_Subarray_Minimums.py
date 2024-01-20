class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        answer = 0

        for currId in range(len(arr) + 1):
            while stack and (currId == len(arr) or arr[stack[-1]] >= arr[currId]):
                midId = stack.pop()
                leftId = stack[-1] if stack else -1
                rightId = currId

                count = (midId - leftId) * (rightId - midId)

                answer += (count * arr[midId]) % MOD
                answer %= MOD
            stack.append(currId)

        return answer
