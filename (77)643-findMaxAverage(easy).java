/* 643. Maximum Average Subarray I
 * Nov 19, 2024
 * Beats 82.41% Runtime (3ms)
 * Beats 84.51% Memory
 */

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double firstSum = 0;
        for (int i = 0; i < k; i++) {
            firstSum += nums[i];
        }

        double maxSum = firstSum;
        double currentSum = firstSum;
        for (int i = 0; i < nums.length - k; i++) {
            currentSum -= nums[i];
            currentSum += nums[i + k];
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
        }

        return maxSum / k;
    }
}
