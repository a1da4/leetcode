class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            score1, ch1, score2, ch2 = x, "ab", y, "ba"
        else:
            score1, ch1, score2, ch2 = y, "ba", x, "ab"
        answer = 0
        stack1 = []
        for ch in s:
            stack1.append(ch)
            while len(stack1) > 1 and stack1[-2] + stack1[-1] == ch1:
                stack1.pop()
                stack1.pop()
                answer += score1
        
        stack2 = []
        for ch in stack1:
            stack2.append(ch)
            while len(stack2) > 1 and stack2[-2] + stack2[-1] == ch2:
                stack2.pop()
                stack2.pop()
                answer += score2

                
        return answer

