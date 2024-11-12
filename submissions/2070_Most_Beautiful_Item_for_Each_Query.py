class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[1], reverse=True)
        answer = []
        for query in queries:
            is_added = False
            for price, beauty in items:
                if query >= price:
                    answer.append(beauty)
                    is_added = True
                    break
            if not is_added:
                answer.append(0)

        return answer

