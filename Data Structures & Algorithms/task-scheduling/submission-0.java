
class Solution {
    private PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
            (a, b) -> b.getValue() - a.getValue());

    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> taskCounts = new HashMap<>();
        for (char task : tasks) {
            taskCounts.put(task, taskCounts.getOrDefault(task, 0) + 1);
        }
        pq.addAll(taskCounts.entrySet());

        int counter = 0;
        while (!pq.isEmpty()) {
            int i = 0;
            List<Map.Entry<Character, Integer>> tempList = new ArrayList<>();
            while (i <= n) {
                if (!pq.isEmpty()) {
                    Map.Entry<Character, Integer> entry = pq.poll();
                    entry.setValue(entry.getValue() - 1);
                    if (entry.getValue() > 0) {
                        tempList.add(entry);
                    }
                }
                i++;
                counter++;
                if (pq.isEmpty() && tempList.isEmpty()) {
                    break;
                }
            }
            pq.addAll(tempList);
        }
        return counter;
    }
}
