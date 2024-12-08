class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        vocab = set(words)
        
        def dfs(currWord: str):
            if currWord in memo:
                return memo[currWord]
            maxLen = 1
            for i in range(len(currWord)):
                newWord = currWord[:i] + currWord[i + 1:]
                if newWord in vocab:
                    currentLen = 1 + dfs(newWord)
                    maxLen = max(maxLen, currentLen)
            memo[currWord] = maxLen

            return maxLen

        return max(dfs(word) for word in words)

