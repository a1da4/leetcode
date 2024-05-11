class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxLen = 0
        queue = deque([])
        for ch in s:
            queue.append(ch)
            while queue and len(set(queue)) > k:
                queue.popleft()
            maxLen = max(maxLen, len(queue))
        
        return maxLen
