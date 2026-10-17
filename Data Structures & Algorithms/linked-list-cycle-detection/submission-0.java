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
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visitedNodes = new HashSet<>();

        ListNode iterNode = head;
        while(iterNode!=null){
            if(visitedNodes.contains(iterNode)){
                return true;
            }
            visitedNodes.add(iterNode);
            iterNode = iterNode.next;
        }

        return false;
    }
}
