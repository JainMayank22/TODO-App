# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #  Initialize Empty List and Variables
        ans = ListNode(None)
        prev = ans
        sum1 = 0
        carry = 0
        #  check for any LinkedList empty or not
        while l1!=None or l2!=None:
            sum1 = carry
            # check for individual list if not then add its val
            if l1!=None:
                sum1 += l1.val
                l1 = l1.next
            if l2!=None:
                sum1 += l2.val
                l2 = l2.next
            #  to store the carry 
            carry = int(sum1/10)
            prev.next = ListNode(sum1%10)
            prev = prev.next
        # Carry remaining if any at last 
        if carry>0:
            prev.next = ListNode(carry)
        return ans.next
        
        