class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        for currAsteroid in asteroids:
            while answer and answer[-1] > 0 and currAsteroid < 0:
                if answer[-1] + currAsteroid < 0:
                    answer.pop()
                elif answer[-1] + currAsteroid > 0:
                    break
                else:
                    answer.pop()
                    break
            else:
                answer.append(currAsteroid)
        
        return answer
