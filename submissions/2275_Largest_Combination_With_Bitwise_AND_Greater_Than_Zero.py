class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        numBit = [0] * 32

        for num in candidates:
            bNum = bin(num)[2:][::-1]
            for i in range(len(bNum)):
                if bNum[i] == "1":
                    numBit[i] += 1
        
        return max(numBit)

