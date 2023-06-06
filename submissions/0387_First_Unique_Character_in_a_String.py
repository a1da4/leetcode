class Solution:
    def firstUniqChar(self, s: str) -> int:
        vocab = set()
        uniqChars = []

        for char in s:
            if char not in vocab:
                uniqChars.append(char)
                vocab.add(char)
            else:
                if char in uniqChars:
                    uniqChars.remove(char)
        
        if len(uniqChars) == 0:
            return -1
        else:
            return s.index(uniqChars[0])
