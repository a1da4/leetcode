class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        prev = []
        for num in nums:
            curr = [num]
            for p in prev:
                curr.append(p + num)

            prev[:] = curr
            sums += curr

        return sum([num for num in sorted(sums)[left - 1:right]]) % (10**9 + 7)

