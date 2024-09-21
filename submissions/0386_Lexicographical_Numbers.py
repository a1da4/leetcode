class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = [str(num) for num in range(1, n + 1)]

        return [int(ch) for ch in sorted(arr)]
        
