class Solution {
    public boolean validTree(int n, int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        HashSet<Integer> visits = new HashSet<>();
        
        for (int[] edge: edges) {
            List<Integer> list = adj.getOrDefault(edge[0], new ArrayList<>());
            list.add(edge[1]);
            adj.put(edge[0], list);

            List<Integer> list2 = adj.getOrDefault(edge[1], new ArrayList<>());
            list2.add(edge[0]);
            adj.put(edge[1], list2);
        }

        if (!dfs(0, -1, adj, visits)) {
            return false;
        }

        return visits.size() == n;
    }

    private boolean dfs(int n, int p, Map<Integer, List<Integer>> adj, HashSet<Integer> visits) {
        if (visits.contains(n)) {
            return false;
        }
        visits.add(n);
        
        List<Integer> list = adj.getOrDefault(n, new ArrayList<>());
        for (int neighbor : list) {
            if (neighbor != p) {
                if (!dfs(neighbor, n, adj, visits)) {
                    return false;
                }
            }
        }
        return true;
    }
}
