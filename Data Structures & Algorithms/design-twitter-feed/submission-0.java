class Twitter {
    private Map<Integer, List<int[]>> tweet;
    private Map<Integer, Set<Integer>> follow;
    private int count;

    public Twitter() {
        tweet = new HashMap<>();
        follow = new HashMap<>();
        count = 0;
    }

    public void postTweet(int userId, int tweetId) {
        tweet.putIfAbsent(userId, new ArrayList<>());
        tweet.get(userId).add(new int[] { tweetId, count++ });
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new ArrayList<>();
        List<int[]> temp = new ArrayList<>();

        follow.putIfAbsent(userId, new HashSet<>());
        follow.get(userId).add(userId);

        for (int followeeId : follow.get(userId)) {
            if (tweet.containsKey(followeeId)) {
                temp.addAll(tweet.get(followeeId));
            }
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[1], a[1]));
        pq.addAll(temp);
        int i = 0;
        while (!pq.isEmpty() && i < 10) {
            res.add(pq.poll()[0]);
            i++;
        }
        return res;
    }

    public void follow(int followerId, int followeeId) {
        follow.putIfAbsent(followerId, new HashSet<>());
        follow.get(followerId).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (follow.containsKey(followerId)) {
            follow.get(followerId).remove(followeeId);
        }
    }
}