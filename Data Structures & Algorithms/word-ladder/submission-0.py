class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n=len(wordList)
        m=len(wordList[0])
        adj=collections.defaultdict(list)
        for i in wordList:
            for j in range(m):
                word=i[:j]+'*'+i[j+1:]
                adj[word].append(i)
        q=deque([beginWord])
        visit=set()
        res=1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word==endWord:
                    return res
                for j in range(m):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for jj in adj[pattern]:
                        if jj not in visit:
                            q.append(jj)
            res+=1
        return 0
                    







        