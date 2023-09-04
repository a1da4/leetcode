class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        currCands = products
        currWord = ""
        currLength = 0
        for i in range(len(searchWord)):
            currWord += searchWord[i]
            currLength += 1
            currCands = [cand for cand in currCands if cand[:currLength]==currWord]

            answer.append(currCands[:3])

        return answer
