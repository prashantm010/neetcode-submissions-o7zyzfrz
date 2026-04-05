class DSU {
    int[] parent;
    int[] rank;

    public DSU(int n) {
        this.parent = new int[n + 1];
        this.rank = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            this.parent[i] = i;
            this.rank[i] = 0;
        }
    }

    public int find(int x) {
        if (x == this.parent[x]) {
            return x;
        }

        return parent[x] = this.find(parent[x]);
    }

    public void union(int x, int y) {
        int x_p = this.find(x);
        int y_p = this.find(y);

        if (x_p == y_p) {
            return;
        }

        if (rank[x_p] > rank[y_p]) {
            parent[y_p] = x_p;
        } else if (rank[x_p] < rank[y_p]) {
            parent[x_p] = y_p;
        } else {
            parent[y_p] = x_p;
            rank[x_p]++;
        }
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;

        DSU dsu = new DSU(n);

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            if (dsu.find(u) == dsu.find(v)) {
                return edge;
            }
            dsu.union(u, v);
        }

        return new int[] {};
    }
}
