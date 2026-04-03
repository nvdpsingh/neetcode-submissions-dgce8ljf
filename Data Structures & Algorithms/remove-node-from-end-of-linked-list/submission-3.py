# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        arr = []
        
        while curr:
            arr.append(curr)
            curr=curr.next
        
        prev = arr[len(arr) - n - 1] 
        prev.next=prev.next.next

        return dummy.next