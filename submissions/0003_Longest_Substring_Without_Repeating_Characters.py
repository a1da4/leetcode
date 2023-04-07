# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        temp_substr = set()
        max_length = 0

        for i in range(len(s)):
            temp_substr.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in temp_substr:
                    temp_length = len(temp_substr)
                    max_length = max(temp_length, max_length)
                    temp_substr = set()
                    break
                temp_substr.add(s[j])
            temp_length = len(temp_substr)    
            max_length = max(temp_length, max_length)

        return max_length
