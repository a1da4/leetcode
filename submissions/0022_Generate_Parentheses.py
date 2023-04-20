class Solution:
    # add ( or ) instead of adding () at once
    def updateParenthesis(self, listParens: List[str], maxLength: int) -> List[str]:
        updatedParens = []
        for tempParens in listParens:
            numLeftParens = tempParens.count("(")
            numRightParens = len(tempParens) - numLeftParens
            if numLeftParens < maxLength:
                updatedParens.append(tempParens+"(")
            if numRightParens < maxLength and numLeftParens > numRightParens:
                updatedParens.append(tempParens+")")
        
        return updatedParens

    def generateParenthesis(self, n: int) -> List[str]:
        answer = ["("]
        for i in range(2*n-1):
            answer = self.updateParenthesis(answer, n)
            answer = list(set(answer))
            print(answer)

        return answer
