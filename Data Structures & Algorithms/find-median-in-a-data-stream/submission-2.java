class MedianFinder {
    PriorityQueue<Integer> rightMinHeap;
    PriorityQueue<Integer> leftMaxHeap;

    public MedianFinder() {
        this.rightMinHeap = new PriorityQueue<>();
        this.leftMaxHeap = new PriorityQueue<>(Collections.reverseOrder());
    }

    public void addNum(int num) {
        if (leftMaxHeap.isEmpty() || num < this.leftMaxHeap.peek()) {
            this.leftMaxHeap.offer(num);
        } else {
            this.rightMinHeap.offer(num);
        }

        if (leftMaxHeap.size() < rightMinHeap.size()) {
            this.leftMaxHeap.offer(this.rightMinHeap.poll());
        } else if (leftMaxHeap.size() - rightMinHeap.size() > 1) {
            this.rightMinHeap.offer(this.leftMaxHeap.poll());
        }
    }

    public double findMedian() {
        int size = this.leftMaxHeap.size() + this.rightMinHeap.size();

        if (size % 2 == 0) {
            return (this.leftMaxHeap.peek() + this.rightMinHeap.peek()) / 2.0;
        }

        return this.leftMaxHeap.peek();
    }
}
