# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = "/".join(startUrl.split("/")[:3])
        self.domain = domain
        self.domLen = len(domain)
        visited = {startUrl}
        try:
            htmlParser.getUrls(domain)
            visited.add(domain)
        except:
            pass

        queue = deque([domain, startUrl])
        while queue:
            N = len(queue)
            for _ in range(N):
                url = queue.popleft()
                try:
                    urls = htmlParser.getUrls(url)
                    if urls == []:
                        continue
                    for _url in urls:
                        if len(_url) < self.domLen:
                            continue
                        if _url[:self.domLen] != self.domain:
                            continue
                        if _url not in visited:
                            visited.add(_url)
                            queue.append(_url)
                except:
                    continue

        return list(visited)

