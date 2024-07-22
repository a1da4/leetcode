class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightIds = sorted([(height, heightId) for \
                             heightId, height in \
                             enumerate(heights)],
                            key=lambda x:x[0],
                            reverse=True)
        return [names[heightId[1]] for heightId in heightIds]
