class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        targets = [w for w, c in Counter(arr).items() if c == 1]

        return targets[k - 1] if len(targets) >= k else ""
