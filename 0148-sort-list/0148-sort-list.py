# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):

        
        if head is None or head.next is None:
            return head

        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        mid = slow.next
        slow.next = None

        
        left = self.sortList(head)
        right = self.sortList(mid)

        
        return self.merge(left, right)

    def merge(self, a, b):

        dummy = ListNode(0)
        tail = dummy

        while a and b:

            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        
        if a:
            tail.next = a
        else:
            tail.next = b

        return dummy.next
        

        
        