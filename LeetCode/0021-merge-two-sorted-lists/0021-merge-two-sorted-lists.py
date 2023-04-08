# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = answer = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                list2, answer.next = list2.next, list2
            
            else:
                list1, answer.next = list1.next, list1
            
            answer = answer.next
        
        if list1:
            answer.next = list1
        
        if list2:
            answer.next = list2
        
        return head.next