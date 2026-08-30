'''Detect cycle in linked list'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"->",end=" ")
            curr=curr.next
            
    def detectloop(self,head):
        slow=fast=head
        while slow and fast:

            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
            
        return False            


head=Node(1)            
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=head.next

if head.detectloop(head):
    print("True")
else:
    print("False")    



