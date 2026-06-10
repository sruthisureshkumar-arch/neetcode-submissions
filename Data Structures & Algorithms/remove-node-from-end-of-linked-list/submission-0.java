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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){
            return null;
        }
        int count = 0;
        ListNode temp = head;
        while(temp != null){
            count++;
            temp = temp.next;
        }
        if(count ==n){
            return head.next;
        }
        int res= count - n;
        temp =head;
        while(temp != null){
            res--;
            if(res == 0){
                break;
            }
            temp = temp.next;
        }
        temp.next = temp.next.next;
        return head;
    }
    public void printLL(ListNode head){
        System.out.println("[");
        if(head != null){
        while(head.next != null){
            System.out.println(head.val+",");
        }
        System.out.println(head.val);
        }
        System.out.println("]");

    }
}