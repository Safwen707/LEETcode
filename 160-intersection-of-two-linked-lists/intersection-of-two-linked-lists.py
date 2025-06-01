# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def Len(self,head:ListNode)-> int:
        chead=head
        s=0
        while chead!= None:
            s+=1
            chead=chead.next
        return s


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ch="No intersection"
        cheadA=headA
        cheadB=headB

        LenA=self.Len(headA)
        LenB=self.Len(headB)
        if LenA<LenB:
            if cheadB:
                for i in range(LenB-LenA):
                    cheadB=cheadB.next
        if LenA>LenB:
            if cheadA:
                for i in range(LenA-LenB):
                    cheadA=cheadA.next
        if LenA==1 and LenB==1:
            if headA.val==headB.val:
                return headA
        while cheadA and cheadB:
            if cheadB==cheadA :
                print(cheadB)
                print(cheadA)

                

                
                return cheadA
            else:
                cheadB=cheadB.next
                cheadA=cheadA.next
        return None


        
        