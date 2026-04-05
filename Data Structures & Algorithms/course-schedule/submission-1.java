class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] node: prerequisites) {
            List<Integer> pre = new ArrayList();
            if (map.containsKey(node[0])) {
                pre = map.get(node[0]);
            }
            pre.add(node[1]);
            map.put(node[0], pre);
        }

        Set<Integer> visits = new HashSet<>();   

        for (int x=0; x<numCourses; x++) {
            if (!dfs(map, visits, x)) {
                return false;
            }
        }

        return true;
    }

    private boolean dfs(Map<Integer, List<Integer>> map, Set<Integer> visits, int node) {
        if (visits.contains(node)) {
            return false;
        }
        if (map.getOrDefault(node, new ArrayList<>()).isEmpty()) {
            return true;
        }
        
        visits.add(node);
        for (int pre: map.get(node)) {
            if (!dfs(map, visits, pre)) {
                return false;
            }
        }
        visits.remove(node);
        map.put(node, new ArrayList<>());

        return true;
    }
}
