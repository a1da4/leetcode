class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []

        def search(s, curr):
            if s == "":
                answer.append(" ".join(curr))
                return
            for word in wordDict:
                if len(word) <= len(s) and word == s[:len(word)]:
                    search(s[len(word):], curr + [word])
        
        search(s, [])
        return answer
