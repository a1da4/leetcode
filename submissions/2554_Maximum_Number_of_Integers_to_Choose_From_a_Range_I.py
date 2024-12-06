class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        answer = []
        currSum = 0
        for num in range(1, n + 1):
            if num in banned:
                continue
            if currSum + num > maxSum:
                break
            currSum += num
            answer.append(num)

        return len(answer)

