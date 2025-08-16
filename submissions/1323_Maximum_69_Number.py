class Solution:
    def maximum69Number (self, num: int) -> int:
        digit = int(math.floor(math.log10(num)))
        while digit >= 0:
            curr = 10 ** digit
            if (num // curr) % 10 == 6:
                num += curr * 3
                break
            digit -= 1

        return num
