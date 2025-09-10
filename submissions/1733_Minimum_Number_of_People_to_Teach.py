class Solution:
    def minimumTeachings(
        self, 
        n: int, 
        languages: List[List[int]], 
        friendships: List[List[int]],
    ) -> int:
        m = len(languages)
        answer = m
        languages_fixed = [set(lang) for lang in languages]

        friendships_fixed = []
        for friend1, friend2 in friendships:
            lang1 = languages_fixed[friend1 - 1]
            lang2 = languages_fixed[friend2 - 1]
            if len(lang1 & lang2) == 0:
                friendships_fixed.append(
                    [friend1 - 1, friend2 - 1]
                )
        
        for language in range(1, n + 1):
            required = set()
            for friend1, friend2 in friendships_fixed:
                if language not in languages_fixed[friend1]:
                    required.add(friend1)

                if language not in languages_fixed[friend2]:
                    required.add(friend2)

            answer = min(answer, len(required))

        return answer
