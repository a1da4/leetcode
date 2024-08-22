class Solution:
    def findComplement(self, num: int) -> int:
        bNum = bin(num)
        head = bNum[:2]
        digit = ''.join(['1' if ch == '0' else '0' for ch in bNum[2:]])

        return int(head + digit, 2)

