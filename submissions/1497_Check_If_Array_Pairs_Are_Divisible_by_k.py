class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rests = [0] * k
        for num in arr:
            rest = num % k
            _rest = k - rest if rest > 0 else 0
            if rests[_rest] > 0:
                rests[_rest] -= 1
            else:
                rests[rest] += 1

        return sum(rests) == 0

