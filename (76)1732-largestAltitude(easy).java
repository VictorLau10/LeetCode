/* 1732. Find the Highest Altitude
 * Nov 25, 2024
 * Beats 100% Runtime (0ms)
 * Beats 56.23% Memory
 */

class Solution {
    public int largestAltitude(int[] gain) {
        int max = 0;
        int altitude = 0;
        for (int i = 0; i < gain.length; i++) {
            altitude += gain[i];
            if (altitude > max) {
                max = altitude;
            }
        }
        return max;
    }
}
