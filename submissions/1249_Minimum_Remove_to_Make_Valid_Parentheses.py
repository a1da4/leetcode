class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        curr = 0
        answer = ""
        for ch in s:
            if ch == "(":
                answer += ch
                curr += 1
            elif ch == ")":
                if curr <= 0:
                    continue
                else:
                    answer += ch
                    curr -= 1
            else:
                answer += ch
        
        answer = answer[::-1].replace("(", "", curr)[::-1]

        return answer
