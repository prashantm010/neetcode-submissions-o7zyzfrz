class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> {
            int d1 = a[0] * a[0] + a[1] * a[1];
            int d2 = b[0] * b[0] + b[1] * b[1];
            return d2 - d1;
        });

        for (int[] point : points) {
            q.offer(point);

            while (q.size() > k) {
                q.poll();
            }
        }
        int[][] ans = new int[k][2];

        for (int i = 0; i < k; i++) {
            ans[i] = q.poll();
        }

        return ans;
    }
}
