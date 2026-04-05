class Solution {
    int maxLength = 0;
    int start = 0;
    int end = 0;
    boolean[][] dp = new boolean[1001][1001];

    private boolean isPallindrome(String s, int x, int y) {
        if (x >= y) {
            return true;
        }
        if (dp[x][y] != false) {
            return dp[x][y];
        }
        char c1 = s.charAt(x);
        char c2 = s.charAt(y);
        if (c1 == c2) {
            dp[x][y] = isPallindrome(s, x + 1, y - 1);
            return dp[x][y];
        }
        dp[x][y] = false;
        return dp[x][y];
    }

    public String longestPalindrome(String s) {
        int n = s.length();
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (isPallindrome(s, i, j)) {
                    if ((j - i + 1) > maxLength) {
                        maxLength = j - i + 1;
                        start = i;
                        end = j;
                    }
                }
            }
        }
        return s.substring(start, end + 1);
    }
}
