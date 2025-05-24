class Solution:
    def findWordsContaining(
        self, 
        words: List[str], 
        x: str,
    ) -> List[int]:

        return [
            wordId for wordId, word in enumerate(words)
            if x in word
        ]
