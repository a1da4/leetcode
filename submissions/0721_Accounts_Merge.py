class Solution:
    def update(
        self,
        currName: str,
        mail2accountIds: Dict[str, List[int]],
        startId: int,
        currId: int,
        accounts: List[List[str]],
        answer: List[List[str]],
    ) -> List[List[str]]:
        graph = defaultdict(set)
        for mergedIds in mail2accountIds.values():
            if len(mergedIds) == 1:
                continue
            M = len(mergedIds)
            for i in range(M):
                for j in range(i + 1, M):
                    graph[mergedIds[i]].add(mergedIds[j])
                    graph[mergedIds[j]].add(mergedIds[i])
            
        visited = set()
        for accountId in range(startId, currId):
            if accountId in visited:
                continue
            queue = deque([accountId])
            mergedIds = []
            while queue:
                mergedId = queue.popleft()
                mergedIds.append(mergedId)
                visited.add(mergedId)
                for nextId in graph[mergedId]:
                    if nextId in visited:
                        continue
                    queue.append(nextId)
            
            mails = []
            for mergedId in mergedIds:
                mails += accounts[mergedId][1:]
            
            answer.append(
                [currName] + sorted(list(set(mails)))
            )
        return answer

    def accountsMerge(
        self, 
        accounts: List[List[str]],
    ) -> List[List[str]]:
        answer = []
        
        mail2accountIds = defaultdict(list)
        startId = 0
        accounts.sort(key=lambda x:x[0])
        currName = accounts[0][0]

        for currId, account in enumerate(accounts):
            if account[0] != currName:
                answer = self.update(
                    currName, 
                    mail2accountIds,
                    startId,
                    currId,
                    accounts,
                    answer,
                )

                startId = currId
                mail2accountIds = defaultdict(list)
                currName = account[0]

            for mail in set(account[1:]):
                mail2accountIds[mail].append(currId)

        answer = self.update(
            currName, 
            mail2accountIds,
            startId,
            len(accounts),
            accounts,
            answer,
        )

        return answer

