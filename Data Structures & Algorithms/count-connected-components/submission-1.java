class Solution {
    public int countComponents(int n, int[][] edges) {
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

        int result = 0;
        for (int i=0; i < n; i++) {
            if (!visits.contains(i)) {
                visits.add(i);
                dfs(i, adj, visits);
                result++;
            }
        }
        
        return result;
    }

    private void dfs(int n, Map<Integer, List<Integer>> adj, HashSet<Integer> visits) {
        List<Integer> list = adj.getOrDefault(n, new ArrayList<>());
        for (int i=0; i<list.size(); i++) {
            if (!visits.contains(list.get(i))) {
                visits.add(list.get(i));
                dfs(list.get(i), adj, visits);
            }
        }
    }
}
