class Solution:
    def findAllRecipes(
        self, 
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
    ) -> List[str]:
        answer = []

        supplies = set(supplies)
        queue = deque([(recipe, ingredient) 
                    for recipe, ingredient in zip(recipes, ingredients)])

        while queue:
            N = len(queue)
            updated = False
            for _ in range(N):
                recipe, requirements = queue.popleft()
                if all([requirement in supplies for requirement in requirements]):
                    answer.append(recipe)
                    supplies.add(recipe)
                    updated = True
                else:
                    queue.append((recipe, requirements))
            
            if not updated:
                break

        return answer

