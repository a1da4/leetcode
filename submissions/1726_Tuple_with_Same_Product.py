class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod2freq = {}
        N = len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                num_i, num_j = nums[i], nums[j]
                prod = num_i * num_j
                if prod not in prod2freq:
                    prod2freq[prod] = 0
                prod2freq[prod] += 1

        answer = 0
        for prod, freq in prod2freq.items():
            if freq >= 2:
                answer += freq * (freq - 1) * 4

        return answer

