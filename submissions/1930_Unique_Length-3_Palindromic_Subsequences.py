class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        characters = set(s)
        answer = 0
        for ch in characters:
            middles = set()
            for mid in range(s.index(ch) + 1, s.rindex(ch)):
                middles.add(s[mid])
            
            answer += len(middles)

        return answer

