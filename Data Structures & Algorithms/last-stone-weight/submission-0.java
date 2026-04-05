class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int stone : stones) {
            pq.add(stone);
        }
        while (pq.size() > 1) {
            int x = pq.poll();
            int y = pq.poll();
            int diff = x - y;
            if (diff > 0) {
                pq.add(diff);
            }
        }
        return pq.size() == 0 ? 0 : pq.peek();
    }
}
