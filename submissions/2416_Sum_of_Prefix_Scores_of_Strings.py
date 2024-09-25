class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        chs = []
        for word in words:
            while word:
                chs.append(word)
                word = word[:-1]
            
        ch2score = Counter(chs)
        scores = []
        for word in words:
            score = 0
            while word:
                score += ch2score[word]
                word = word[:-1]
            scores.append(score)

        return scores

