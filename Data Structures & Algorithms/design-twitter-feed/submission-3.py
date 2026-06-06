class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time,tweetId])
        self.time -= 1



        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.jj=[]
        res=[]
        self.followMap[userId].add(userId)
        for i in self.followMap[userId]:
            if i in self.tweetMap:
                index=len(self.tweetMap[i])
                if index>0:
                    time,tid=self.tweetMap[i][index-1]
                    heapq.heappush(self.jj,[time,tid,index-1,i])

        while self.jj and len(res)<10:
            time,tid,index,ide=heapq.heappop(self.jj)
            res.append(tid)
            if index>=1:
                time,tid=self.tweetMap[ide][index-1]
                heapq.heappush(self.jj,[time,tid,index-1,ide])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
