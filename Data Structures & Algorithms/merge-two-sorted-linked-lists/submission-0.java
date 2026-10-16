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
        ListNode head;

        if(list1==null && list2==null) {
            return list1;
        } else if(list1==null){
            return list2;
        } else if (list2==null) {
            return list1;
        }

        if(list1.val<list2.val) {
            head = list1;
            list1 = list1.next;
        } else {
            head = list2;
            list2 = list2.next;
        }

        ListNode iteratingNode = head;

        while(list1!=null && list2!=null){
            ListNode nextNode;
            if(list1.val<list2.val) {
                nextNode = list1;
                list1 = list1.next;
            } else {
                nextNode = list2;
                list2 = list2.next;
            }

            iteratingNode.next = nextNode;
            iteratingNode = iteratingNode.next;
        }

        if(list1!=null) {
            iteratingNode.next = list1;
        } else {
            iteratingNode.next = list2;
        }

        return head;
    }
}