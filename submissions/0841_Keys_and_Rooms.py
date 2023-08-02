class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        numRooms = len(rooms)
        openedRooms = [0] * numRooms
        openedRooms[0] = 1
        visitedRooms = set()

        def visitRoom(key, rooms, openedRooms, visitedRooms):
            if key in visitedRooms:
                return openedRooms, visitedRooms
            
            visitedRooms.add(key)
            openedRooms[key] = 1
            nextKeys = rooms[key]

            for key in nextKeys:
                openedRooms, visitedRooms = visitRoom(key, rooms, openedRooms, visitedRooms)

            return openedRooms, visitedRooms
        
        openedRooms, _ = visitRoom(0, rooms, openedRooms, visitedRooms)

        return all(openedRooms)
