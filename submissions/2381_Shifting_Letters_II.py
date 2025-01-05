class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ordA, ordZ = ord("a"), ord("z")
        N = len(s)

        moves = [0] * N
        for shift in shifts:
            sign = 1 if shift[2] else -1
            moves[shift[0]] += sign
            if shift[1] + 1 < N:
                moves[shift[1] + 1] -= sign

        chrs = []
        numMove = 0
        for i, move in enumerate(moves):
            numMove = (numMove + move) % (ordZ - ordA + 1)
            if numMove < 0:
                numMove += (ordZ - ordA + 1)
            
            chrs.append(chr((ord(s[i]) - ordA + numMove) % (ordZ - ordA + 1) + ordA))
 
        return "".join(chrs)

