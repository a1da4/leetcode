class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        is_removed = 0
        for char in s[::-1]:
            if char == "*":
                is_removed += 1
            elif is_removed:
                is_removed -= 1
            else:
                answer.append(char)
        
        return "".join(answer[::-1])
