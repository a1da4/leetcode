class Solution:
    def countCompleteSubarrays(
        self, 
        nums: List[int],
    ) -> int:
        N = len(nums)
        S = len(set(nums))
        num2freq = {}
        s = 0
        answer = 0
        r = 0

        for l in range(N):
            while r < N and s < S:
                num = nums[r]
                num2freq[num] = num2freq.get(num, 0) + 1
                if num2freq[num] == 1:
                    s += 1
                r += 1
            if s == S:
                answer += N - r + 1
            num = nums[l]
            num2freq[num] -= 1
            if num2freq[num] == 0:
                s -= 1

        return answer

