class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        pm = {"+", "-"}
        lefts = []
        rights = []

        def _helper(ch, stack):
            right = ""
            left = ""
            isRight = True
            while stack:
                _ch = stack.pop()
                if _ch == "/":
                    isRight = False
                elif _ch in pm:
                    left, right = int(left), int(right)
                    if _ch == "-":
                        left *= -1
                    lefts.append(left)
                    rights.append(right)
                    left, right = "", ""     
                    break
                elif isRight:
                    right = _ch + right
                else:
                    left = _ch + left
            if left and right:
                left, right = int(left), int(right)
                lefts.append(left)
                rights.append(right)
                
        for chId, ch in enumerate(expression):
            if ch in pm:
                _helper(ch, stack)

            stack.append(ch)

        _helper(ch, stack)
        
        def lcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        rightLcm = functools.reduce(lcm, rights)
        leftSum = 0
        for left, right in zip(lefts, rights):
            leftSum += left * (rightLcm // right)

        if leftSum == 1 or leftSum == -1:
            _gcd = 1
        elif leftSum == 0:
            _gcd = 1
            rightLcm = 1
        else:
            _gcd = math.gcd(abs(leftSum), rightLcm)

        return str(leftSum // _gcd) + "/" + str(rightLcm // _gcd)
