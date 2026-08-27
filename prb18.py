class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")


    def comparing(self,head1,head2):
        curr1,curr2=head1,head2
        temp1,temp2=head1,head2
        new_head=None
        while curr1 !=None and curr2 !=None :
            if curr1.data < curr2.data :
                temp1=curr1
                curr1=curr1.next
                temp1.next=None
                new_head=self.merge_node(temp1,new_head)
            else:
                temp2=curr2
                curr2=curr2.next
                temp2.next=None
                new_head=self.merge_node(temp2,new_head)

        while curr1 != None:
            while new_head.next !=None:
                new_head=new_head.next
            new_head.next=curr1

            while curr2 != None:
                while new_head.next !=None:
                    new_head=new_head.next
                    new_head.next=curr2
        return new_head

    def merge_node(self,temp,new_head):
            if new_head==None:
                new_head=temp
            else:
                new_curr=new_head
                while new_curr.next!=None:
                    new_curr=new_curr.next
                new_curr.next=temp
            return new_head
          


head1=Node(1)            
head1.next=Node(4)
head1.next.next=Node(6)

head2=Node(2)
head2.next=Node(3)
head2.next.next=Node(5)
head2.next.next=Node(7)


head1.traveral(head1)
head2.traveral(head2)
ans=head1.comparing(head1,head2)
head1.traveral(ans)



