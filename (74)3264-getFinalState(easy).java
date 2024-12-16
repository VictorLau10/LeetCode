/* 3264. Final Array State After K Multiplication Operations
 * Dec 16, 2024
 * Beats 34.22% Runtime (3ms, O(n^2) > my O(n log n) in this case due to low constraints)
 * Beats 7.25% Memory
 */

import java.util.PriorityQueue;
import java.lang.Comparable;

class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        // Input all values of nums into priority queue as a pair (value, index)
        PriorityQueue<Pair> pq = new PriorityQueue<>(nums.length, new PairComparator());
        for (int i = 0; i < nums.length; i++) {
            Pair newPair = new Pair(nums[i], i);
            pq.add(newPair);
        }

        // Executing operation (in place of nums)
        for (int i = 0; i < k; i++) {
            Pair minValue = pq.poll();
            nums[minValue.getIndex()] *= multiplier;
            minValue.setValue(minValue.getValue() * multiplier);
            pq.add(minValue);  // add the multiplied value back into the pq
        }

        return nums;
    }

    // Nested pair class to make index accessible through priority queue
    public class Pair {
        int value;
        int index;
        public Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
        public int getValue() {
            return value;
        }
        public int getIndex() {
            return index;
        }
        public void setValue(int value) {
            this.value = value;
        }
    }

    // Nested comparator class for comparing pair values
    public class PairComparator implements Comparator<Pair> {
        public int compare(Pair p1, Pair p2) {
            if (p1.getValue() < p2.getValue()) {
                return -1;
            } else if (p1.getValue() == p2.getValue()) {
                if (p1.getIndex() < p2.getIndex()) {
                    return -1;
                } else if (p1.getIndex() > p2.getIndex()) {
                    return 1;
                } else {
                    return 0;
                }
            } else {
                return 1;
            }
        }
    }
}
