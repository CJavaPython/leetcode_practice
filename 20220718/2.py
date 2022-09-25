#2. Add Two Numbers
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def forward(l1, l2, up=0, digits=1):
            result = []
            if l1.next==None:
                return []
            result.append(((l1.val+l2.val)%10)*digits)
            forward_list = forward(l1.next, l2.next, (l1.val+l2.val)/10, digits*10)
            for f in forward_list:
                result.append(f)
            return result        
        result = forward(l1,l2,up=0,digits=1)
        
        return result
        
s=Solution()
l1=ListNode(2)
forwarder = l1
for value in [4,3]:
    print(value)
    new_node=ListNode(value)
    forwarder.next=new_node
    forwareder = forwarder.next
#print(l1.next.next.val)
l2=ListNode(5)
forwarder = l2
for value in [6,4]:
    new_node=ListNode(value)
    forwarder.next=new_node
    forwareder = forwarder.next
checker = l1
while checker:
    print(checker.val)
    checker = checker.next
print(s.addTwoNumbers(
    l1, l2
))