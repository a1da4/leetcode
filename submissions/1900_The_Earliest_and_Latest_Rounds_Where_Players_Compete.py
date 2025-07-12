class Solution:
    def earliestAndLatest(
        self, 
        n: int, 
        firstPlayer: int, 
        secondPlayer: int,
    ) -> List[int]:
        p1, p2 = firstPlayer-1, secondPlayer-1

        @lru_cache(None)
        def dfs(mask: int) -> Tuple[int, int]:
            alives = [i for i in range(n) if (mask >> i) & 1]
            m = len(alives)
            id1, id2 = alives.index(p1), alives.index(p2)
            if id1 + id2 == m - 1:
                return (1, 1)

            next_masks = set()

            def backtrack(
                next_id1: int, 
                next_id2: int, 
                curr_mask: int,
            ) -> None:
                if next_id1 > next_id2:
                    next_masks.add(curr_mask)
                    return

                next_p1, next_p2 = alives[next_id1], alives[next_id2]
                if next_p1 in (p1, p2) or next_p2 in (p1, p2):
                    winner = next_p1 if next_p1 in (p1, p2) else next_p2
                    backtrack(
                        next_id1 + 1, 
                        next_id2 - 1, 
                        curr_mask | (1 << winner),
                    )
                else:
                    for winner in [next_p1, next_p2]:
                        backtrack(
                            next_id1 + 1, 
                            next_id2 - 1, 
                            curr_mask | (1 << winner),
                        )

            backtrack(0, m - 1, 0)
            earliest_rounds, latest_rounds = float('inf'), 0
            for next_mask in next_masks:
                earlier_rounds, later_rounds = dfs(next_mask)
                earliest_rounds = min(earliest_rounds, earlier_rounds)
                latest_rounds = max(latest_rounds, later_rounds)
            return (earliest_rounds + 1, latest_rounds + 1)

        return list(dfs((1 << n) - 1))

