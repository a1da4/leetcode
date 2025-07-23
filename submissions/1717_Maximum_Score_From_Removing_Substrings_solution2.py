class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            score1, ch1, score2, ch2 = x, "ab", y, "ba"
        else:
            score1, ch1, score2, ch2 = y, "ba", x, "ab"
        answer = 0
        stack1 = deque([])
        for ch in s:
            if stack1 and stack1[-1] + ch == ch1:
                stack1.pop()
                answer += score1
            else:
                stack1.append(ch)
        
        stack2 = deque([])
        for ch in stack1:
            if stack2 and stack2[-1] + ch == ch2:
                stack2.pop()
                answer += score2
            else:
                stack2.append(ch)

        return answer

