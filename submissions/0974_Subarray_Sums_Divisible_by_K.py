class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        mod = 0
        mod2freq = Counter()
        mod2freq[0] += 1
        for num in nums:
            mod = (mod + num % k + k) % k
            answer += mod2freq[mod]
            mod2freq[mod] += 1

        return answer
