/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(0);
        ListNode* curr = res;

        int carry = 0;
        while(l1 || l2 || carry) {
            int digit1 = 0, digit2 = 0;

            if(l1) {
                digit1 = l1->val;
                l1 = l1->next;
            }
            if(l2) {
                digit2 = l2->val;
                l2 = l2->next;
            }

            int sum = digit1 + digit2 + carry;
            int digit = sum%10;
            carry = sum/10;
            curr->val = digit;

            if(carry || l1 || l2) {
                curr->next = new ListNode(0);
                curr = curr->next;
            }


        return res;
    }
};
