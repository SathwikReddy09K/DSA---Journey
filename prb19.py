'''Reversing kth node from 1st with kth node from last'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def counting_nodes(self,head):
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        return count    
 
        
    def swapping_kth_node(self,head,kth_first,kth_last):
        count=1
        curr=head
        while curr:
            if kth_first==count:
                firstK_node=curr
                count+=1
                curr=curr.next

            if kth_last==count:
                curr.data,firstK_node.data=firstK_node.data,curr.data
                
                
            
            curr=curr.next
            count+=1

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
head.traveral(head)

count=head.counting_nodes(head)
print(count)

k=int(input("Enter k value:"))

lastKth_node=count-k+1


new_head=head.swapping_kth_node(head,k,lastKth_node)

new_head.traveral(new_head)