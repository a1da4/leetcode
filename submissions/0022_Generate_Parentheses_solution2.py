class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = [("", 0)]
        for i in range(n):
            numParenthese = len(parentheses)
            for _ in range(numParenthese):
                currParenthese, numRight = parentheses.pop(0)
                currParenthese += "("
                if i + 1 < n:
                    parentheses.append((currParenthese, numRight))
                    for j in range(numRight, i+1):
                        currParenthese += ")"
                        parentheses.append((currParenthese, j + 1))
                else:
                    for j in range(numRight, i+1):
                        currParenthese += ")"
                    parentheses.append((currParenthese, i + 1))
            
        return [pare_num[0] for pare_num in parentheses]
