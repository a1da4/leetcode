class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        currNum = 0

        for currChar in s:
            if currChar == "[":
                stack.append(currStr)
                stack.append(currNum)
                currStr = ""
                currNum = 0
            elif currChar == "]":
                num = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + num * currStr
            elif currChar in "1234567890":
                currNum = currNum * 10 + int(currChar)
            else:
                currStr += currChar
        
        return currStr
