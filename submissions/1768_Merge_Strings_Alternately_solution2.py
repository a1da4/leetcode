class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        word1 = deque(word1)
        word2 = deque(word2)
        while word1 or word2:
            if word1:
                answer += word1.popleft()
            if word2:
                answer += word2.popleft()
        
        return answer

