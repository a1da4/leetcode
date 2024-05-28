class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        S = len(s)
        boldIds = [False] * S
        
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    boldIds[i] = True
                    
                start = s.find(word, start + 1)

        answer = []
        
        for i in range(S):
            if boldIds[i] and (i == 0 or boldIds[i - 1] is False):
                answer.append("<b>")
                
            answer.append(s[i])
            
            if boldIds[i] and (i == S - 1 or boldIds[i + 1] is False):
                answer.append("</b>")
        
        return "".join(answer)
