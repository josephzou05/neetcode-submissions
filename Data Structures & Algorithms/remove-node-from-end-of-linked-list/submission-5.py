# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        #1) find length of the list
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        #2) remove the (length - n)th node in the list
        curr = head
        location = 0
        if n == length:
            return head.next
        while curr:
            location += 1
            if location == (length - n):
                temp = curr.next.next
                curr.next = temp
                break
            curr = curr.next
        return head
