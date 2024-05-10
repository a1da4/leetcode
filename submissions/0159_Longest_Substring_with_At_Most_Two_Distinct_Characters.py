class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maxLen = 0
        queue = deque([])
        for ch in s:
            queue.append(ch)
            while queue and len(set(queue)) > 2:
                queue.popleft()
            maxLen = max(maxLen, len(queue))
        
        return maxLen
