class KthLargest {
    private PriorityQueue<Integer> minHeap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();

        for (Integer num: nums) {
            this.minHeap.offer(num);
            while (this.minHeap.size() > k) {
                this.minHeap.poll();
            }
        }
    }
    
    public int add(int val) {
        this.minHeap.offer(val);
        while (this.minHeap.size() > k) {
            this.minHeap.poll();
        } 
        return this.minHeap.peek();
    }
}
