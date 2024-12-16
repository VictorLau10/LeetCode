/* 1106. Parsing a Boolean Expression
 * Oct 20, 2024
 * Beats 9.19% Runtime
 * Beats 5.84% Memory
 */

import java.util.Stack;

class Solution {

    // make stack
    // for every char in expression
        // push current char
        // if char is a back facing bracket
            // pop until we reach a front facing bracket
            // evaluate operation
            // push operation inside stack (as either a 't' or 'f')

    public boolean parseBoolExpr(String expression) {
        Stack<Character> s = new Stack<Character>();

        for (int i = 0; i < expression.length(); i++) {
            Character current = expression.charAt(i);
            s.push(current);
            if (current == ')') {
                String str = "";
                while (s.peek() != '(') {
                    str += s.pop();
                }
                s.pop();
                Character operator = s.pop();
                if (evaluateExpr(str, operator)) {
                    s.push('t');
                } else {
                    s.push('f');
                }
            }
        }

        if (s.pop() == 't') {
            return true;
        } else {
            return false;
        }
    }

    public boolean evaluateExpr(String expr, Character operator) {
        if (operator == '&') {
            for (int i = 0; i < expr.length(); i++) {
                if (expr.charAt(i) == 'f') {
                    return false;
                }
            }
            return true;
        } else if (operator == '|') {
            for (int i = 0; i < expr.length(); i++) {
                if (expr.charAt(i) == 't') {
                    return true;
                }
            }
            return false;
        } else if (operator == '!'){
            // requires the operation inside to be a single letter
            for (int i = 0; i < expr.length(); i++) {
                if (expr.charAt(i) == 'f') {
                    return true;
                } else if (expr.charAt(i) == 't') {
                    return false;
                }
            }
        }
        return false;
    }
}
