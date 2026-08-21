class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")


node1=Node(1)            
node2=Node(2)
node3=Node(1)
node4=Node(1)
node5=Node(2)
node6=Node(1)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None

head=node1

print("original single linkedlist:")
head.traveral(head)



