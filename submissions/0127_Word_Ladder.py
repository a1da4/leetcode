from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord:
            return 0
        
        if not wordList:
            return 0

        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        allCombinationDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                allCombinationDict[word[:i] + "*" + word[i+1:]].append(word)

        queue = [[beginWord, 1]]
        visited = {beginWord: True}
        visitedVocab = set()
        visitedVocab.add(beginWord)
        while queue:
            currentWord, step = queue.pop(0)
            for i in range(L):
                interWord = currentWord[:i] + "*" + currentWord[i+1:]

                for word in allCombinationDict[interWord]:
                    if word == endWord:
                        return step + 1
                    if word not in visitedVocab:
                        visited[word] = True
                        visitedVocab.add(word)
                        queue.append([word, step + 1])
                
                allCombinationDict[interWord] = []

        return 0

