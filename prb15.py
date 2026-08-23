'''Deleting node in the linked list'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def deleting_node(self,head,val):
        if head.data==val:
            temp=head
            head=head.next
            temp.next=None
            return head
        curr=head
        prev=curr
        while curr!= None :
            if curr.data==val:
                prev.next=curr.next
                curr.next=None
            prev=curr
            curr=curr.next
        return head
node1=Node(10)            
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None

head=node1

print("original single linked list:")
head.traveral(head)

val=int(input("Enter a value to delete the node:"))

ans=head.deleting_node(head,val)
print("After deleting the node:")
head.traveral(ans)


