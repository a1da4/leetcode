class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        mod = 10 ** 9 + 7
        memo = {}

        def trip(currId: int) -> int:
            if currId < 0:
                return 1
            if currId in memo:
                return memo[currId]
            if s[currId] == "*":
                count = 9 * trip(currId - 1) % mod
                if currId > 0:
                    if s[currId - 1] == "1":
                        count += 9 * trip(currId - 2) % mod
                    elif s[currId - 1] == "2":
                        count += 6 * trip(currId - 2) % mod
                    elif s[currId - 1] == "*":
                        count += 15 * trip(currId - 2) % mod
                    else:
                        pass
                    count %= mod
                memo[currId] = count
                return count
            else:
                count = 0 if s[currId] == "0" else trip(currId - 1)
                if currId > 0:
                    if (s[currId - 1] == "1"
                        or (s[currId - 1] == "2" and s[currId] <= "6")):
                        count += trip(currId - 2) % mod
                    elif s[currId - 1] == "*":
                        count += ((2 if s[currId] <= "6" else 1) * trip(currId - 2)) % mod
                    else:
                        pass
                    count %= mod
                memo[currId] = count
                return count

        return trip(N - 1)

