/* 2. Add Two Numbers
 * Sep 27, 2024
 * Beats 14.87% Runtime (2ms)
 * Beats 87.39% Memory
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean carryBit = false;
        int sum = l1.val + l2.val;
        if (sum >= 10) {
            carryBit = true;
            sum -= 10;
        }
        ListNode head = new ListNode(sum);
        ListNode temp = head;

        while (l1.next != null || l2.next != null || carryBit) {
            // If next node is null, create a placeholder '0'
            ListNode placeHolder = new ListNode(0);
            if (l1.next == null) {
                l1.next = placeHolder;
            }
            if (l2.next == null) {
                l2.next = placeHolder;
            }
            l1 = l1.next;
            l2 = l2.next;

            sum = l1.val + l2.val;
            if (carryBit) {
                carryBit = false;
                sum += 1;
            }
            if (sum >= 10) {
                carryBit = true;
                sum -= 10;
            }

            ListNode newNode = new ListNode(sum);
            temp.next = newNode;
            temp = temp.next;
        }

        return head;
    }
}
