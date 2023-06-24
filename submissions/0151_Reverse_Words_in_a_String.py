class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        for currChar in s.strip().split()[::-1]:
            if len(currChar) == 0:
                continue
            
            answer.append(currChar)
        
        return " ".join(answer)
