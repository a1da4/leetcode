class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino2freq = {}
        for dice_1, dice_2 in dominoes:
            if dice_1 > dice_2:
                dice_1, dice_2 = dice_2, dice_1
            
            if (dice_1, dice_2) not in domino2freq:
                domino2freq[(dice_1, dice_2)] = 1
            else:
                domino2freq[(dice_1, dice_2)] += 1
        
        answer = 0
        for freq in domino2freq.values():
            if freq > 1:
                answer += (freq * (freq - 1)) // 2
        
        return answer

