class Solution:
    def canVisitAllRooms(
        self, 
        rooms: List[List[int]],
    ) -> bool:
        visited = set()
        n = len(rooms)

        queue = deque([0])

        while queue:
            room = queue.popleft()
            visited.add(room)
            for nextRoom in rooms[room]:
                if nextRoom in visited:
                    continue
                queue.append(nextRoom)

        return len(visited) == n
