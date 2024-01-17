class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n2f = Counter(arr)
        return len(n2f) == len(Counter(n2f.values()))
