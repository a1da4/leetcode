class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        numWords = len(words)
        wordLength = len(words[0])
        
        ref = Counter(words)

        i = 0
        while i <= len(s) - numWords*wordLength:
            if s[i:i+wordLength] not in set(words):
                i += 1
                continue
            
            temp = []
            for j in range(i, i+wordLength*numWords, wordLength):
                temp.append(s[j:j+wordLength])
            pred = Counter(temp)
            if pred == ref:
                answer.append(i)

            i += 1

        return answer
