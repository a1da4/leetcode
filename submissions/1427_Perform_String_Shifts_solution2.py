class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        totalamount = 0
        for direction, amount in shift:
            if direction == 1:
                totalamount -= amount
            else:
                totalamount += amount

        totalamount %= len(s)
        return s[totalamount:] + s[:totalamount]

