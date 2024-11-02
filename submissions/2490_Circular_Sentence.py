class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if words[0][0] != words[-1][-1]:
            return False
        
        for w1, w2 in zip(words[:-1], words[1:]):
            if w1[-1] != w2[0]:
                return False
        
        return True
