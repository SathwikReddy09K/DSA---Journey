class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def move_upto_kplace(self,head,k):
            curr=head
            count=0
            while curr!=None and count < k:
                curr=curr.next
                count+=1
            fast=curr
            return fast   
        
    def swapping_kth_node(self,head,fast):
            slow=head
            while fast!=None:
                slow=slow.next
                fast=fast.next
            slow.data,fast.data=fast.data,slow.data
            return head    
         

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

head=node1

print("Original single linkedlist:")
node1.traveral(head)

k=int(input("Enter k value:"))

fast=head.move_upto_kplace(head,k)

print("kth node value from the single linkedlist:",end=" ")
head.swapping_kth_node(head,fast)

head.traveral(head)