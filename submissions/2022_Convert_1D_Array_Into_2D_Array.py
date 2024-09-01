class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        mat = []
        curr = 0
        for _ in range(m):
            mat.append(original[curr:curr + n])
            curr += n

        return mat

