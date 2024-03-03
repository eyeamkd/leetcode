# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the linked list
        # Because I am a stupid person
        # prev = None
        # while(head):
        #     if head.next==None:
        #         head.next = prev 
        #         break 
        #     nextElement = head.next 
        #     head.next = prev 
        #     prev = head 
        #     head = nextElement
         
        # print("Head is", head) 

        temp = head 
        res = []

        while temp:
            res.append(temp.val)
            temp = temp.next 
        
        temp = head
        prev = None
        position = len(res)-n+1
        value = res[-n]
        counter = 1
        print("Value is", value)
        while(temp):
            if counter==position:
                if prev:
                    prev.next = temp.next
                else:
                    head = temp.next 
            else:
                prev = temp 
            temp = temp.next 
            counter+=1
  
        return head 
        