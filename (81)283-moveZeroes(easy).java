/* 283. Move Zeroes
 * Oct 17, 2024
 * Beats 24.09% Runtime
 * Beats 44.01% Memory
 */

class Solution {
    public void moveZeroes(int[] nums) {
        // head elem = 0
        // While we have not made it to the end of the list
            // If current num is not 0
                // Add to the index head elem
            // Go to next number
        
        // fill in rest of zeroes
        int head = 0;
        int i = 0;
        while (i < nums.length) {
            if (nums[i] != 0 && i == head) {
                head++;
            } else if (nums[i] != 0 && i > head) {
                nums[head] = nums[i];
                head++;
            }
            i++;
        }
        for (int j = head; j < nums.length; j++) {
            nums[j] = 0;
        }
    }
}
