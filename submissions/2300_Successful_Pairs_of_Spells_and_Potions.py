class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = sorted([(spell, index) for index, spell in enumerate(spells)])
        sortedPotions = sorted(potions)
        numPotions = len(potions)
        currentIndex = numPotions - 1
        answer = [0] * len(spells)

        #for spell in spells:
        for spell, index in sortedSpells:
            #answer.append(sum([1 if spell*potion >= success else 0 for potion in potions]))
            if sortedPotions[0] * spell >= success:
                answer[index] += numPotions
            elif sortedPotions[-1] * spell < success:
                answer[index] = 0
            else:
                while currentIndex >= 0 and sortedPotions[currentIndex] * spell >= success:
                    currentIndex -= 1
                answer[index] += (numPotions - currentIndex - 1)        
        return answer
