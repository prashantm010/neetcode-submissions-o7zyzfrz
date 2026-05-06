class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int num : stones) {
            minHeap.offer(num);
        }

        while (minHeap.size() > 1) {
            int f = minHeap.poll();
            int s = minHeap.poll();
            if (f - s != 0) {
                minHeap.offer(Math.abs(f-s));
            }
        }
        return minHeap.size() > 0 ? minHeap.peek() : 0;
    }
}
