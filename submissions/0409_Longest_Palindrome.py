class Solution:
    def longestPalindrome(self, s: str) -> int:
        is_odd = False
        answer = 0
        for _, freq in Counter(s).most_common():
            if freq % 2:
                if not is_odd:
                    answer += freq
                    is_odd = True
                else:
                    answer += freq - 1
            else:
                answer += freq
        return answer

