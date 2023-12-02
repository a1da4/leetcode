class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(f"0b{a}", 0) + int(f"0b{b}", 0))[2:]  
