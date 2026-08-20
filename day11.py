class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")
    def Middle_node(self,head):
        fast=head
        slow=head
        while fast!=None:
            if(fast.next!=None):
                fast=fast.next.next
                slow=slow.next
            else:   
                return slow.data
        return slow.data


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

print("Original single linkedlist:")
head.traveral(head)

print("Middle node data of single linkedlist:")
ans=head.Middle_node(head)
print(ans)


