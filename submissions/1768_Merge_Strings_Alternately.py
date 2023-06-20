class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        length1 = len(word1)
        length2 = len(word2)

        for i in range(max(length1, length2)):
            if i < length1:
                mergedWord += word1[i]
            if i < length2:
                mergedWord += word2[i]
        
        return mergedWord
