class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        numZero = 0
        for num in nums:
            if num == 0:
                numZero += 1
            else:
                answer += ((numZero + 1) * numZero) // 2
                numZero = 0
        if numZero > 0:
            answer += ((numZero + 1) * numZero) // 2

        return int(answer)
