
class Solution:
    def find(
        self,
        parent: List[int],
        accountId: int,
    ) -> int:
        while parent[accountId] != accountId:
            parent[accountId] = parent[parent[accountId]]
            accountId = parent[accountId]
    
        return accountId
    
    def union(
        self,
        parent: List[int],
        accountId1: int,
        accountId2: int,
    ) -> List[int]:
        accountId1 = self.find(parent, accountId1)
        accountId2 = self.find(parent, accountId2)
        if accountId1 != accountId2:
            parent[accountId2] = accountId1

        return parent
    
    def update(
        self,
        currName: str,
        mail2accountIds: Dict[str, List[int]],
        startId: int,
        currId: int,
        accounts: List[List[str]],
        answer: List[List[str]],
    ) -> List[List[str]]:
        parent = list(range(currId - startId))
        for mergedIds in mail2accountIds.values():
            if len(mergedIds) == 1:
                continue
            
            first = mergedIds[0] - startId
            for mergedId in mergedIds[1:]:
                other = mergedId - startId
                parent = self.union(parent, first, other)

        graph = defaultdict(set)
        for accountId in range(startId, currId):
            curr = accountId - startId
            root = self.find(parent, curr)
            rootId = root + startId
            graph[rootId].add(accountId)
        
        for rootId, mergedIds in graph.items():
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

