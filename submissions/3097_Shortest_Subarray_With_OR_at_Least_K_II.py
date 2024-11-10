class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minLength = float("inf")
        start = end = 0
        bits = [0] * 32

        def _update(bits: list, number: int, delta: int) -> None:
            for pos in range(32):
                if number & (1 << pos):
                    bits[pos] += delta

        def _convert(bits: list) -> int:
            result = 0
            for pos in range(32):
                if bits[pos]:
                    result |= 1 << pos

            return result

        while end < len(nums):
            _update(bits, nums[end], 1)
            while start <= end and _convert(bits) >= k:
                minLength = min(minLength, end - start + 1)
                _update(bits, nums[start], -1)
                start += 1
            end += 1

        return -1 if minLength == float("inf") else minLength



