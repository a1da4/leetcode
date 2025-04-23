class Solution:
    def countLargestGroup(self, n: int) -> int:
        digitSum2count = Counter()
        for num in range(1, n + 1):
            digitSum = 0
            while num > 0:
                digit = num % 10
                digitSum += digit
                num //= 10
            digitSum2count[digitSum] += 1

        maxCount = max(digitSum2count.values())

        return Counter(
            digitSum2count.values()
        )[maxCount]

