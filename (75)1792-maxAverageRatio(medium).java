/* 1792. Maximum Average Pass Ratio
 * Dec 16, 2024
 * Beats 99.93% Runtime
 * Beats 82.80% Memory
 */

import java.util.PriorityQueue;
import java.lang.Comparable;

class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<Pair> gainedRatios = new PriorityQueue<Pair>(classes.length, new PairComparator());
        
        // Add all classes inside 'gainedRatios'
        for (int i = 0; i < classes.length; i++) {
            double addedRatio = (double) (classes[i][0] + 1) / (double) (classes[i][1] + 1);
            double oldRatio = (double) classes[i][0] / (double) classes[i][1];

            Pair pair = new Pair(addedRatio - oldRatio, i);
            gainedRatios.add(pair);
        }

        for (int i = 0; i < extraStudents; i++) {
            // retrieve maximum value
            Pair highestRatioPair = gainedRatios.poll();
            int highestRatioIndex = highestRatioPair.getIndex();
            
            double oldRatio = (double) (classes[highestRatioIndex][0] + 1) / (double) (classes[highestRatioIndex][1] + 1);
            
            // change original ratio in 'classes' to new ratio in place
            classes[highestRatioIndex][0] += 1;
            classes[highestRatioIndex][1] += 1;
            double newRatio = (double) (classes[highestRatioIndex][0] + 1) / (double) (classes[highestRatioIndex][1] + 1);

            Pair newPair = new Pair(newRatio - oldRatio, highestRatioIndex);
            gainedRatios.add(newPair);
        }
        
        // Summation of classes
        double total = 0;
        for (int i = 0; i < classes.length; i++) {
            total += (double)classes[i][0] / (double)classes[i][1];
        }
        
        return total / classes.length;
    }

    // Nested pair class to make index accessible through priority queue
    public class Pair {
        double ratio;
        int index;
        public Pair(double ratio, int index) {
            this.ratio = ratio;
            this.index = index;
        }
        public double getRatio() {
            return ratio;
        }
        public int getIndex() {
            return index;
        }
    }

    // Nested comparator class for comparing pair values
    public class PairComparator implements Comparator<Pair>{
        public int compare(Pair p1, Pair p2) {
            if (p1.getRatio() < p2.getRatio()) {
                return 1;
            } else if (p1.getRatio() == p2.getRatio()) {
                return 0;
            } else {
                return -1;
            }
        }
    }
}
