class Solution {
    int res = 0;
    public int subsetXORSum(int[] nums) {
        backtrack(0, 0, nums);
        return res;
    }

    public void backtrack(int index, int currXorr, int[] nums) {
        res += currXorr;

        for (int i = index; i < nums.length; i++) {
            backtrack(i + 1, currXorr ^ nums[i], nums);
        }
    }
}