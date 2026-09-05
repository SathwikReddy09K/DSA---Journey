class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"->",end=" ")
            curr=curr.next
        print("NULL")    

    def add(self,head1,head2):
        curr1=head1
        curr2=head2
        while curr1 and curr2:
                curr1.data+=curr2.data
                curr1=curr1.next
                curr2=curr2.next

        
        return head1        

head1=Node(1)            
head1.next=Node(2)
head1.next.next=Node(3)
head1.next.next.next=Node(4)

head2=Node(5)            
head2.next=Node(6)
head2.next.next=Node(7)
head2.next.next.next=Node(8)


print("Original single linked list 1:")
head1.traveral(head1)

print("Original single linked list 2:")
head2.traveral(head2)

head=head1.add(head1,head2)

print("After adding two each nodes:")
head1.traveral(head1)