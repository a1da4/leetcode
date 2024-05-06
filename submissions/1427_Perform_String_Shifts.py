class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        totalamount = 0
        for direction, amount in shift:
            if direction == 1:
                totalamount -= amount
            else:
                totalamount += amount

        if totalamount > 0:
            totalamount %= len(s)
            s = s[totalamount:] + s[:totalamount]
            return s
        elif totalamount < 0:
            totalamount %= len(s)
            s = s[totalamount:] + s[:totalamount]
            return s
        else:
            return s

