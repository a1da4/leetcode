class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set()
        for ch in brokenLetters:
            broken.add(ch)
        
        answer = 0
        for word in text.split():
            state = 1
            for ch in word:
                if ch in broken:
                    state = 0
                    break
            
            answer += state
        
        return answer

