class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [num for num in range(1, n + 1)]
        currId = 0

        while nums:
            currId = (currId + k - 1) % n
            num = nums.pop(currId)
            n -= 1

        return num

