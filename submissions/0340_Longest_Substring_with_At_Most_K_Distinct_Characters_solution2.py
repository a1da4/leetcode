class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxLen = 0
        char2freq = Counter()

        for rightId in range(len(s)):
            char2freq[s[rightId]] += 1
            if len(char2freq) <= k:
                maxLen += 1
            else:
                char2freq[s[rightId - maxLen]] -= 1
                if char2freq[s[rightId - maxLen]] == 0:
                    char2freq.pop(s[rightId - maxLen]) 
        return maxLen
