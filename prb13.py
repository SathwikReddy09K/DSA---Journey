'''checking given linked list is palindrome'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def reversing(self,head2):
            prev=None
            curr=head2
            while curr!=None:
               next_node=curr.next
               curr.next=prev
               prev=curr
               curr=next_node
            head2=prev
    
            return head2


    def compersion(self,head1,head2):
            curr1=head1
            curr2=head2
            while curr1  and curr2 :
                if curr1.data !=curr2.data:
                    return False
                
                curr1=curr1.next
                curr2=curr2.next
    
            return True 

node1=Node(1)            
node2=Node(2)
node3=Node(3)
node4=Node(3)
node5=Node(2)
node6=Node(1)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None

copy1=Node(1)            
copy2=Node(2)
copy3=Node(3)
copy4=Node(3)
copy5=Node(2)
copy6=Node(1)

copy1.next=copy2
copy2.next=copy3
copy3.next=copy4
copy4.next=copy5
copy5.next=copy6
copy6.next=None

head=node1
head2=copy1

print("original single linkedlist:")
head.traveral(head)

head2=head2.reversing(head2)
head2.traveral(head2)


print("Given single linkedlist is palindrome :")
ans=head2.compersion(head,head2)

if ans:
    print("True")
else:
    print("False")      




