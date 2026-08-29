class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traveral(self,curr):
        while curr!=None:
            print(curr.data,"-<",end=" ")
            curr=curr.next
        print("NULL")

    def compare_odd_even(self,head):

        odd_tail=even_tail=head
        odd_head=even_head=None
        curr=head

        while(curr !=None):

            if curr.data % 2 !=0:

                if even_head!=None:
                    prev_even,prev_odd=prev_odd,prev_even
                curr_odd=curr_odd.next
            

            else:
                prev_even=curr_even.data
                curr_even=curr_even.next

        return head       

head=Node(17)
head.next=Node(15)
head.next.next=Node(8)
head.next.next.next=Node(7)
head.next.next.next.next=Node(2)
head.next.next.next.next.next=Node(4)
head.next.next.next.next.next.next=Node(6)

print("single linked list:")
head.traveral(head)

ans=head.compare_odd_even(head)
head.traveral(ans)

