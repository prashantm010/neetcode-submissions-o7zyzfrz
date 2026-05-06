class Twitter:
    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.counter, tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        heap = []
        for user in self.followMap[userId]:
            if user in self.tweetMap:
                for count, tweet in self.tweetMap[user]:
                    heapq.heappush(heap, [count, tweet])

        res = []
        while heap and len(res) < 10:
            count, tweet = heapq.heappop(heap)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
