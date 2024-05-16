class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        if sentence1 == sentence2:
            return True
        similarPairs = set([(pair[0], pair[1]) for pair in similarPairs])
        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2 or (word1, word2) in similarPairs or (word2, word1) in similarPairs:
                continue
            else:
                return False

        return True

