class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        currCounter = Counter(words[0])
        currVocab = set(words[0])

        for word in words[1:]:
            currVocab = currVocab & set(word)
            for ch, freq in Counter(word).items():
                if ch in currVocab:
                    currCounter[ch] = min(currCounter[ch], freq)

        answer = []
        if currVocab:
            for ch in list(currVocab):
                answer = answer + [ch] * currCounter[ch]
        return answer
