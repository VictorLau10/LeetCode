/* 21. Nerge Two Sorted Lists
 * Sep 30, 2024
 * Beats 100% Runtime (1ms, invalid comparison)
 * Beats 56.67% Memory
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Null checks
        if (list1 == null && list2 == null) {
            return list1;
        } else if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        }

        ListNode dummyHead = new ListNode();
        ListNode iterator = dummyHead;

        // Iterate through both lists and append smaller value
        while (list1 != null && list2 != null) {
            if (list2.val < list1.val) {
                ListNode newNode = new ListNode(list2.val);
                iterator.next = newNode;
                list2 = list2.next;
            } else {
                ListNode newNode = new ListNode(list1.val);
                iterator.next = newNode;
                list1 = list1.next;
            }
            iterator = iterator.next;
        }

        // Append the remaining values
        while (list1 != null) {
            ListNode newNode = new ListNode(list1.val);
            iterator.next = newNode;
            list1 = list1.next;
            iterator = iterator.next;
        }
        while (list2 != null) {
            ListNode newNode = new ListNode(list2.val);
            iterator.next = newNode;
            list2 = list2.next;
            iterator = iterator.next;
        }

        return dummyHead.next;
    }
}
