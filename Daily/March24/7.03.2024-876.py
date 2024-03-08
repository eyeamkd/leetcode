# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        stack = [] 
        
        while(head!=None):
            stack.append(head)
            head = head.next 
            
        length = len(stack) 
        
        if(length>0):
            # if(length%2==0):
            #     return stack[length//2 -1] 
            return stack[length//2] 
        return 0