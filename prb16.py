'''Reversing only specificed position  nodes'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")


    def finding_nodes(self,head,m,n):
        curr=head
        count=0
        while curr != None :
            count+=1
            if count==m:
                temp1=curr.data
                new_node=curr

            elif count==n:
                temp2=curr.data
                curr.data=temp1
                new_node.data=temp2
            
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

print("Original linked list:")
head.traveral(head)

m=int(input("Enter m position:"))
n=int(input("Enter n position:"))
new_head=head.finding_nodes(head,m,n)
head.traveral(new_head)

