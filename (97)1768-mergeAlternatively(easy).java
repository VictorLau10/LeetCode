/* 1768. Merge Strings Alternatively
 * Sep 17, 2024
 * Beats 16.83% Runtime
 * Beats 5.37% Memory
 */

class Solution {
    public String mergeAlternately(String word1, String word2) {
        String s = "";
        for (int i = 0; i < Math.min(word1.length(), word2.length()); i++) {
            if (i < word1.length()) {
                s += word1.charAt(i);
            }
            if (i < word2.length()) {
                s += word2.charAt(i);
            }
        }
        return s;
    }
}
