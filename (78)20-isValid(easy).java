/* 20. Valid Parentheses
 * Oct 21, 2024
 * Beats 42.88% Runtime (3ms)
 * Beats 93.96% Memory
 */

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        String front = "([{";
        String back = ")]}";
        Stack<Character> stack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (back.indexOf(c) == -1) {
                stack.push(c);
            } else {
                if (stack.size() == 0) {
                    return false;
                } 
                if (front.indexOf(stack.pop()) != back.indexOf(c)) {
                    return false;
                }
            }
        }

        return stack.size() == 0;
    }
}
