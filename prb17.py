class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def swap_node(self,head):
        temp1=head
        temp2=head.next
        while temp1 != None and temp2 != None:
            temp1.data,temp2.data=temp2.data,temp1.data
            temp1=temp1.next
            temp2=temp2.next
            temp1=temp2
            temp2=temp2.next
            
        return head

head=Node(1)            
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

head.traveral(head)

ans=head.swap_node(head)

head.traveral(ans)
