class Solution:
    def numDecodings(self, s: str) -> int:
        memo: Dict[str, int] = {}

        def travel(currS: str) -> int:
            if currS == "":
                return 1
            if currS[0] == "0":
                return 0
            if len(currS) == 1:
                return 1
            if currS in memo:
                return memo[currS]
            
            result = 0
            if len(currS) > 1:
                result += travel(currS[1:])
            if len(currS) >= 2 and int(currS[:2]) < 27:
                result += travel(currS[2:])

            memo[currS] = result
            return result
        
        return travel(s)

