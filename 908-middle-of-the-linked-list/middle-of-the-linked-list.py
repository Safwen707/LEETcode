# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        middle=head
        i=0
        while current:
            i+=1
            current=current.next
        for j in range(i//2):
            middle=middle.next
        return middle

            

        