class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        currCands = products
        for i, char in enumerate(searchWord):
            currCands = [cand for cand in currCands if len(cand) > i and cand[i]==char]
            answer.append(currCands[:3])

        return answer
