class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        itemVocab = set()
        answerDict = {}
        for item in strs:
            itemKey = ''.join(sorted(item))
            if itemKey not in itemVocab:
                answerDict[itemKey] = []
                itemVocab.add(itemKey)
            answerDict[itemKey].append(item)
        
        answerList = []
        for itemKey in itemVocab:
            itemList = answerDict[itemKey]
            answerList.append(itemList)
        
        return answerList
