# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1) find middle (last element of 1st list)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2) reverse second list
        curr = slow.next
        prev = None
        slow.next = prev

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #3) add them one by one
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


