class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)        
        curr = sum([1 if blocks[i] == "W" else 0 for i in range(k)])
        answer = curr
        for i in range(N - k):
            curr += 1 if blocks[i + k] == "W" else 0
            curr -= 1 if blocks[i] == "W" else 0
            answer = min(answer, curr)

        return answer

