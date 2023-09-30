class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        numWords = len(words)
        wordLength = len(words[0])
        
        i = 0
        while i <= len(s) - numWords*wordLength:
            if s[i:i+wordLength] not in set(words):
                i += 1
                continue

            temp = deepcopy(words)
            temp.remove(s[i:i+wordLength])
            if len(temp) == 0:
                answer.append(i)
            else:
                currId = i+wordLength
                pred = [s[id:id+wordLength] for id in range(currId, currId+wordLength*(numWords-1), wordLength)]
                if sorted(pred) == sorted(temp):
                    answer.append(i)

            i += 1

        return answer
