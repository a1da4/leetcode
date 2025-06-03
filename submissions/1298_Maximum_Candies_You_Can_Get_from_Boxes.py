class Solution:
    def maxCandies(
        self, 
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        answer = 0
        queue = deque()
        found = set()
        visited = set()
        obtainedKeys = set()

        for box in initialBoxes:
            found.add(box)
            if status[box] == 1:
                queue.append(box)
        
        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            
            answer += candies[box]
            visited.add(box)

            for key in keys[box]:
                if key not in obtainedKeys:
                    obtainedKeys.add(key)
                    if key in found and key not in visited:
                        queue.append(key)
            
            for _box in containedBoxes[box]:
                if _box not in found:
                    found.add(_box)
                    if status[_box] == 1 or _box in obtainedKeys:
                        queue.append(_box)


        return answer
