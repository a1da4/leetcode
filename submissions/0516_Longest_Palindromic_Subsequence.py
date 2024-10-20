class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def search(l: int, r: int):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = search(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(search(l, r - 1), search(l + 1, r))
            return memo[(l, r)]
        
        return search(0, len(s) - 1)
            
