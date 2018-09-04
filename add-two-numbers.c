//https://leetcode.com/problems/add-two-numbers/description/

#include <stdio.h>
#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode * res = malloc(sizeof(struct ListNode));
    struct ListNode * tmp = res;
    
    int carry = 0;
    while(l1!= NULL || l2!= NULL) {
        /*printf("both not null\n");
        printf("    l1: %d\n", l1 ? l1->val : 0);
        printf("    l2: %d\n", l2 ? l2->val : 0);*/
        
        int l1_digit = (!l1 == NULL) ? l1->val : 0;
        int l2_digit = (!l2 == NULL) ? l2->val : 0;
        
        tmp->val = (l1_digit + l2_digit + carry)%10;
        carry = (l1_digit + l2_digit + carry >= 10) ? 1 : 0;
        
        //printf("carry: %d\n", carry);
            
        //printf("setting digitt tto %d\n", tmp->val);
        if(l1 != NULL) {
            printf("l1 not null - going next\n");
            l1 = l1->next;
        }
        if(l2 != NULL) {
            printf("l2 not null - going next\n");
            l2 = l2->next;
        }
        if(l1 != NULL || l2 != NULL) {
            tmp->next = malloc(sizeof(struct ListNode));
            tmp = tmp->next;
        }
        
    }
    //printf("out of loop");
    
    if(carry != 0) {
        tmp->next = malloc(sizeof(struct ListNode));
        tmp = tmp->next;
        tmp->val = carry;
        carry = 0;
    }
    
    tmp->next = NULL;
    //printf("return res");
    return res;
}