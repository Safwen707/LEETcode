# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         curr=head
#         if not curr:
#             return 0
#         if curr.next and not curr.next.next:

#             return curr.val+curr.next.val
#         if not curr.next:
#             return curr.val
#         n=0
#         while curr:
#             n+=1
#             curr=curr.next
#         possible_i=list(range(0,n//2))
#         possible_twin={i:n-1-i for i in possible_i}
#         slow=head
#         Max=0
#         l=[]
#         for i,j in possible_twin.items():
            
            
            
            
            
#             fast=slow  
#             for ji in range(j-i):
#                 fast=fast.next
#             newMax=slow.val+fast.val
#             if Max<newMax:
#                 Max=newMax
#             slow=slow.next
#         return Max


   
                

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # 1. Trouver le milieu
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Inverser la deuxième moitié
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev = début de la 2e moitié inversée
        second = prev
        first = head

        # 3. Calculer les twin sums
        max_sum = 0
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum



        