class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque([])
        answer = 0
        for ch in s:
            if ch == "]":
                if stack:
                    stack.pop()
                else:
                    answer += 1
            else:
                stack.append(ch)
        
        return (answer + 1) // 2 
