class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        L = len(searchWord)
        words = sentence.split()
        for wordId, word in enumerate(words):
            if len(word) >= L and word[:L] == searchWord:
                return wordId + 1
            
        return -1

