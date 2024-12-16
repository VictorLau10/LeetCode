/* 392. Is Subsequence
 * Oct 18, 2024
 * Beats 93.53% Runtime (1ms)
 * Beats 36.20% Memory
 */

class Solution {
    public boolean isSubsequence(String s, String t) {
        // Base cases
        if (s.length() == 0) {
            return true;
        }
        if (t.length() == 0) {
            return false;
        }

        int sPointer = 0;
        int tPointer = 0;
        while (tPointer < t.length()) {
            if (t.charAt(tPointer) == s.charAt(sPointer)) {
                sPointer++;
                if (sPointer == s.length()) {
                    return true;
                }
            }
            tPointer++;
        }
        return false;
    }
}
